# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data = pd.read_csv("dashboard/cleaned_hour_data.csv")
    return data
data_df = load_data()

#Buat Sidebar
with st.sidebar:
    #Filter Tanggal
    st.title('Filter Data')
    min_date = pd.to_datetime(data_df['dateday'].min())
    max_date = pd.to_datetime(data_df['dateday'].max())
    date_range = st.date_input("Select date range", value=(min_date, max_date))
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    data_df = data_df[(pd.to_datetime(data_df['dateday']) >= start_date) & (pd.to_datetime(data_df['dateday']) <= end_date)]

    #Filter Lanjutan
    season_options = data_df['season'].unique()
    selected_seasons = st.sidebar.multiselect('Select seasons:', season_options)
    if selected_seasons :
        data_df = data_df[data_df['season'].isin(selected_seasons)]
    
    #Information
    st.header("Information Profile")
    st.markdown("""
    **Name:** Daffa Suada  
    **Email:** [suadaadaffa@gmail.com](mailto:suadaadaffa@gmail.com)  
    **GitHub:** [github.com/DaffaSuadaa](https://github.com/DaffaSuadaa)
    """)


st.markdown("""
# **Dicoding Data Analysis Project** <span style='font-weight:300;'>(Bike Sharing Dataset)</span>
""", unsafe_allow_html=True)


# st.dataframe(data_df)
st.subheader("User Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    total_user_df = data_df['count'].sum()
    st.metric('Total Users', value=total_user_df)


with col2:
    total_user_casual_df = data_df['casual'].sum()
    st.metric('Casual Users', value=total_user_casual_df)
 
with col3:
    total_user_registered_df = data_df['registered'].sum()
    st.metric('Registered Users', value=total_user_registered_df)


#Dashboard Tahunan
st.subheader("Annual Dashboard")

bikeshareMonthAndYear = data_df.groupby(by=["year", "month"]).agg({"count" : "sum"}).reset_index()
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
bikeshareMonthAndYear['month'] = pd.Categorical(bikeshareMonthAndYear['month'], categories=month_order, ordered=True)

plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='count', data=bikeshareMonthAndYear, hue='year', palette=["orange", "blue"])

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Bike Share Count')
plt.title('Bike Share Count Over Time')
st.pyplot(plt)


#Dashboard Mingguan
st.subheader("Weekly Dashboard")
data_df['weekday'] = pd.Categorical(data_df['weekday'],
                                    categories=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
                                    ordered=True)
bikeshareWeekly = data_df.groupby(by= "weekday", observed= True).agg({"count" : "sum"}).reset_index()
plt.figure(figsize=(10, 6))
plt.bar(bikeshareWeekly["weekday"],bikeshareWeekly["count"], label='Registered',
    color='tab:blue')

plt.xlabel("Weekday")
plt.ylabel("Bike Share Count")
plt.xticks(rotation=45)
plt.title("Count by bikeshare users by day")
st.pyplot(plt)


#Dashboard Korelasi
st.subheader("Correlation Analysis of Bike Usage")

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
st.subheader("Bike Rentals by Weather Condition")
weathersit_data = data_df.groupby(by='weathersit').agg({'count' : 'sum'}).reset_index()

plt.figure(figsize=(10,8))
sns.barplot(x='weathersit', y='count', data= weathersit_data)

plt.title('Bike Rentals by Weather Condition')
plt.xlabel('Weathersit')
plt.ylabel('Bike Share Count')
st.pyplot(plt)


#Dashboard Seasonal Registered and Casual
st.subheader("Seasonal Comparison of Bike Rentals: Registered vs. Casual")
seasonal_casual_registered = data_df.groupby(by='season').agg({'registered':'sum', 'casual' : 'sum'}).reset_index()

plt.figure(figsize=(10,8))
plt.bar(seasonal_casual_registered['season'], seasonal_casual_registered['registered'], label='Registered', color='tab:blue')
plt.bar(seasonal_casual_registered['season'], seasonal_casual_registered['casual'], label='Casual', color='tab:orange')

plt.title('Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Bike Share Count')
plt.legend()
st.pyplot(plt)