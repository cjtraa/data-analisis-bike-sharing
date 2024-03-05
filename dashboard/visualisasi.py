import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
all_data = pd.read_csv('https://raw.githubusercontent.com/cjtraa/data-analisis-bike-sharing/main/dashboard/all_data.csv')

# Filter data by year
year_2011 = all_data[all_data['yr'] == 0]
year_2012 = all_data[all_data['yr'] == 1]

# Calculate total rentals for each year and rental type
total_rentals_2011 = year_2011['cnt'].sum()
total_casual_2011 = year_2011['casual'].sum()
total_registered_2011 = year_2011['registered'].sum()

total_rentals_2012 = year_2012['cnt'].sum()
total_casual_2012 = year_2012['casual'].sum()
total_registered_2012 = year_2012['registered'].sum()

# Create Streamlit sidebar
st.sidebar.header('Filter Options')
rental_type = st.sidebar.selectbox('Select Rental Type', ['Total', 'Casual', 'Registered'])

# Prepare data for plotting
years = ['2011', '2012']
rentals = []
if rental_type == 'Casual':
    rentals.append(total_casual_2011)
    rentals.append(total_casual_2012)
elif rental_type == 'Registered':
    rentals.append(total_registered_2011)
    rentals.append(total_registered_2012)
else:
    rentals.append(total_rentals_2011)
    rentals.append(total_rentals_2012)

# Title for Streamlit app
st.title('Data Visualization: Bike Sharing')

# Plot bar chart for total rentals by year and rental type
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=years, y=rentals, ax=ax1)
plt.title(f'Total Rentals by Year and Rental Type ({rental_type})')
plt.xlabel('Year')
plt.ylabel('Total Rentals')
st.pyplot(fig1)

# Show the dataframe for total rentals by year and rental type
st.write(f'Total Rentals by Year and Rental Type ({rental_type}):')
rentals_data = pd.DataFrame({'Year': years, 'Total Rentals': rentals})
st.write(rentals_data)

# Filter data for the top 5 months with highest cnt in 2011
top_months_2011 = year_2011.groupby('mnth')['cnt'].sum().nlargest(5)

# Plot bar chart for top 5 months with highest cnt
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_months_2011.index, y=top_months_2011.values, palette='viridis', ax=ax2)
plt.title('Top 5 Months with Highest Rentals in 2011')
plt.xlabel('Month')
plt.ylabel('Total Rentals')
st.pyplot(fig2)

# Show the dataframe for top 5 months
st.write('Top 5 Months with Highest Rentals in 2011:')
st.write(top_months_2011.reset_index(name='Total Rentals'))
