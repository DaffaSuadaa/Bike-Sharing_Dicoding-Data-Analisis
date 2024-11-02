# Bike Sharing - Dicoding Data Analisis
## Overview
This project is a data analysis and visualization for the final course of Dicoding’s Data Analysis with Python. It focuses on analyzing bike rental data with two years of historical records (2011 and 2012) from Washington D.C.’s Capital Bikeshare system. The publicly available dataset provides valuable insights into rental patterns, weather influences, and user types, accessible at Capital Bikeshare.


## Objective
**1. Define the question**
- Bagaimana performa penyewaan sepedah dalam beberapa tahun terakhir?
- Bagaimana performa penyewaan sepedah setiap hari dalam seminggu?
- Bagaimana performa penyewaan sepedah dalam hari dan jam?
- Apakah terdapat korelasi antara kondisi cuaca dan performa penyewaan sepedah?
- Adakah pengaruh kondisi cuaca dalam penyewaan sepedah?
- Bagaimana perbandingan antar musim dengan pengguna registered dan casual?

**2. Data Wrangling**
- Gathering Data
- Assessing Data
- Cleaning Data

**3. Exploratory Data Analysis** 
- Create Data Exploration

**4. Visualization & Explanatory Analysis** 
- Create Data Visualization that answer business questions
- Answer Business Questions with Visualizations

**5. Streamlit** 
- Create Dashboard Visualization
- Interactive Filters

## **Insight:**
1. **Bike Usage Trends from 2011 to 2012**
   - There was a positive increase in bike usage from 2011 to 2012.
   - The highest increases during specific months suggest seasonal or external factors influencing bike usage.

2. **Consistent Weekly Usage Trend**
   - Bike rentals throughout the week show a stable pattern, with an average of approximately 143 rentals per day.

3. **Hourly Rental Trends**
   - Bike usage increases significantly during the morning (6-8 AM) and evening (5-6 PM), indicating that bikes are often used for commuting to and from work.

4. **Weather Conditions and Bike Usage Correlation**
   - Temperature shows a positive correlation with bike rentals, suggesting that warmer weather encourages more biking.
   - Conversely, humidity shows a negative correlation with bike rentals, indicating that high humidity makes users less comfortable riding.

5. **Weather Preferences for Biking**
   - Users prefer relatively clear weather and tend to avoid extreme weather conditions.

6. **Seasonal Comparisons**
   - The highest usage occurs during Fall, followed by Summer. Spring and Winter show lower usage, possibly due to less favorable weather conditions.


## Project Structure
- bike-sharing-dataset : Contains raw data in .csv format (day and hour).
- Readme.txt : Contains data documentation.
- dashboard_bike-sharing-dataset.py : This file contains visualization and interactive filter with streamlit.
- notebook_bike-sharing.ipynb : This file contains the dashboard with the analysis results.

## Instalation 
1. Clone this repository
```R
git clone https://github.com/DaffaSuadaa/Bike-Sharing_Dicoding-Data-Analisis-Data.git
```
2. Go to the project directory
```R
cd/Bike-Sharing_Dicoding-Data-Analisis-main
```
3. Run streamlit
```R
streamlit run dashboard_bike-sharing-dataset.py
```
