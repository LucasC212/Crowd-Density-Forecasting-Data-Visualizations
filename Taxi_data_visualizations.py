import pandas as pd
import geopandas as gpd
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data visual for Dataset Description:
df = pd.read_parquet("data/taxi/yellow_tripdata_2017-01.parquet")
print(df.head())

# Parse datetime columns
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Filter for a single day (Jan 2, 2017 for example)
date_filter = '2017-01-02'
pickup_day = df[df['tpep_pickup_datetime'].dt.date == pd.to_datetime(date_filter).date()]
dropoff_day = df[df['tpep_dropoff_datetime'].dt.date == pd.to_datetime(date_filter).date()]

# Extract hour
pickup_day['pickup_hour'] = pickup_day['tpep_pickup_datetime'].dt.hour
dropoff_day['dropoff_hour'] = dropoff_day['tpep_dropoff_datetime'].dt.hour

# Group by hour
pickup_counts = pickup_day.groupby('pickup_hour').size().reset_index(name='pickup_count')
dropoff_counts = dropoff_day.groupby('dropoff_hour').size().reset_index(name='dropoff_count')

# Plot drop-offs
plt.figure(figsize=(10, 5))
sns.lineplot(data=dropoff_counts, x='dropoff_hour', y='dropoff_count', marker="o")
plt.title(f'Hourly Taxi Drop-offs on {date_filter}')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Drop-offs')
plt.xticks(range(0, 24))
plt.grid(True)
plt.tight_layout()
plt.show()

# plot NYC taxi zone shapefile
taxi_zones = gpd.read_file('taxi_zones 2/taxi_zones.shp')

fig, ax = plt.subplots(figsize=(10, 10))
taxi_zones.plot(ax=ax, facecolor="lightgray", edgecolor="black", linewidth=0.5)

ax.set_title("NYC Taxi Zones")
ax.set_axis_off()
plt.show()