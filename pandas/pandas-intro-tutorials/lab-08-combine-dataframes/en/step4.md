# Merge Tables Using a Common Identifier

We will then add the station coordinates to the measurements table using the `merge` function. We will perform a left join on the `location` column.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
