import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Uber data into a pandas DataFrame
uber_data = pd.read_csv('uber_data.csv')

# Explore the structure of the data
print(uber_data.head())  # Display the first few rows
print(uber_data.info())  # Show the summary information

# Convert the date/time column to datetime format
uber_data['datetime'] = pd.to_datetime(uber_data['datetime'])

# Extract additional columns from the datetime column
uber_data['year'] = uber_data['datetime'].dt.year
uber_data['month'] = uber_data['datetime'].dt.month
uber_data['day'] = uber_data['datetime'].dt.day
uber_data['hour'] = uber_data['datetime'].dt.hour

# Analyze the data
total_trips = uber_data.shape[0]
print("Total trips:", total_trips)

# Plot the distribution of trips by hour
plt.figure(figsize=(12, 6))
sns.countplot(x='hour', data=uber_data)
plt.title('Distribution of Uber trips by hour')
plt.xlabel('Hour')
plt.ylabel('Number of trips')
plt.show()

# Calculate the average number of trips per day
daily_trips=uber_data.groupby(['year',  'day'])['datetime'].count().reset_index()
average_daily_trips = daily_trips['datetime'].mean()
print("Average daily trips:", average_daily_trips)

# Plot the trend of daily trips over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='datetime', data=daily_trips)
plt.title('Daily Uber trips over time')
plt.xlabel('Date')
plt.ylabel('Number of trips')
plt.xticks(rotation=45)
plt.show()




