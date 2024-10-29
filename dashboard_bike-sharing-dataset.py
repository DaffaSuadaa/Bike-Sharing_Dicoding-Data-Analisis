# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data = pd.read_csv("Dicoding Proyek Analisis Data/Bike-sharing/bike-sharing-dataset/hour.csv")
    return data
data_df = load_data()

#Mengganti tipe data
chage_type_data = ["dteday"]
for column in chage_type_data :
    data_df[column] = pd.to_datetime(data_df[column])
    
#Mengganti nama column
data_df.rename (columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'hr':'hour',
    'cnt': 'count'
}, inplace= True)

#Menghapus column
drop_col = ['year', 'month', 'weekday']
data_df.drop(columns=drop_col, inplace=True)

#Menambah column berdasarkan dateday
data_df['year'] = data_df['dateday'].dt.year.astype(int)
data_df['month'] = data_df['dateday'].dt.month_name()
data_df['weekday'] = data_df['dateday'].dt.day_name()

#Menghubah keterangan data
data_df['season'] = data_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})


#Buat Sidebar
with st.sidebar:
    #Filter Tanggal
    st.title('Filter Data')
    min_date = pd.to_datetime(data_df['dateday'].min())
    max_date = pd.to_datetime(data_df['dateday'].max())
    date_range = st.date_input("Silahkan pilih tanggal", value=(min_date, max_date))
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    data_df = data_df[(pd.to_datetime(data_df['dateday']) >= start_date) & (pd.to_datetime(data_df['dateday']) <= end_date)]

    #Filter Lanjutan
    st.header('Filter Lanjutan')
    season_options = data_df['season'].unique()
    selected_seasons = st.sidebar.multiselect('Silahkan pilih musim:', season_options)
    if selected_seasons :
        data_df = data_df[data_df['season'].isin(selected_seasons)]
    # else :


#Membuat dashboard streamlit
# st.title('Dicoding Proyek Analisis Data')
# st.header("Bike Sharing Dataset")

st.markdown("""
# **Dicoding Proyek Analisis Data** <span style='font-weight:300;'>(Bike Sharing Dataset)</span>
""", unsafe_allow_html=True)


# st.dataframe(data_df)
st.subheader("Analisis Pengguna")
col1, col2, col3 = st.columns(3)
with col1:
    # st.markdown("""
    # **Total Pengguna**
    # """)
    total_user_df = data_df['count'].sum()
    st.metric('Total Pengguna', value=total_user_df)


with col2:
    # st.markdown("""
    # **Pengguna kasual**
    # """)
    total_user_casual_df = data_df['casual'].sum()
    st.metric('Pengguna kasual', value=total_user_casual_df)
 
with col3:
    # st.markdown("""
    # **Pengguna teregistrasi**
    # """)
    total_user_registered_df = data_df['registered'].sum()
    st.metric('Pengguna teregistrasi', value=total_user_registered_df)


#Dashboard Tahunan
st.subheader("Dashboard Tahunan")
bikeshareMonthAndYear = data_df.groupby(by=["year", "month"]).agg({"count" : "sum"}).reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='count', data=bikeshareMonthAndYear, hue='year')

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Bike Share Count Over Time')
st.pyplot(plt)


#Dashboard Mingguan
st.subheader("Dashboard Mingguan")
data_df['weekday'] = pd.Categorical(data_df['weekday'],
                                    categories=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
                                    ordered=True)
bikeshareWeekly = data_df.groupby(by= "weekday", observed= True).agg({"count" : "sum"}).reset_index()
plt.figure(figsize=(10, 6))
plt.bar(bikeshareWeekly["weekday"],bikeshareWeekly["count"], label='Registered',
    color='tab:blue')

plt.xlabel("weekday")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.title("Count by bikeshare users by day")
st.pyplot(plt)

st.subheader("Dashboard")

#Dashboard Korelasi
st.subheader("Korelasi antara data penggunaan sepeda")

plt.figure(figsize=(8, 3))
sns.scatterplot(x='temp', y='count', data=data_df, alpha=0.5, label='Data Points')
sns.regplot(x='temp', y='count', data=data_df, scatter=False, color='red', label='Trendline')

plt.xlabel('Temperature')
plt.ylabel('Bike Share Count')
plt.title('Correlation between Temperature and Count')
plt.legend()
st.pyplot(plt)

#Atemp
plt.figure(figsize=(8, 3))
sns.scatterplot(x='atemp', y='count', data=data_df, alpha=0.5, label='Data Points')
sns.regplot(x='atemp', y='count', data=data_df, scatter=False, color='red', label='Trendline')

plt.xlabel('Temperature Feels Like')
plt.ylabel('Bike Share Count')
plt.title('Correlation between Feels Like Temperature and Count')
plt.legend()
st.pyplot(plt)

#Humidity 
plt.figure(figsize=(8, 3))
sns.scatterplot(x='hum', y='count', data=data_df, alpha=0.5, label='Data Points')
sns.regplot(x='hum', y='count', data=data_df, scatter=False, color='red', label='Trendline')

plt.xlabel('Humidity')
plt.ylabel('Bike Share Count')
plt.title('Correlation between Humidity and Count')
plt.legend()
st.pyplot(plt)


#Dashboard pengguna berdasarkan suhu
st.subheader("Perbandingan Penyewaan Sepedah Berdasarkan Suhu")
weathersit_data = data_df.groupby(by='weathersit').agg({'count' : 'sum'}).reset_index()

plt.figure(figsize=(10,8))
sns.barplot(x='weathersit', y='count', data= weathersit_data)

plt.title('Jumlah penyewaan sepedah berdasarkan suhu')
plt.xlabel('weathersit')
plt.ylabel('count')
st.pyplot(plt)


#Dashboard Seasonal Registered and Casual
st.subheader("Perbandingan Penyewaan sepedah Seasonal antara Registered dan Casual")
seasonal_casual_registered = data_df.groupby(by='season').agg({'registered':'sum', 'casual' : 'sum'}).reset_index()

plt.figure(figsize=(10,8))
plt.bar(seasonal_casual_registered['season'], seasonal_casual_registered['registered'], label='Registered', color='tab:blue')
plt.bar(seasonal_casual_registered['season'], seasonal_casual_registered['casual'], label='Casual', color='tab:orange')

plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Jumlah penyewaan sepeda berdasarkan musim')
plt.legend()
st.pyplot(plt)