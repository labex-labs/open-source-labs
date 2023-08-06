# Convert Long to Wide Table Format

We will now convert the long format data of air quality to wide format using the `pivot` function.

```python
# Filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# Use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Pivot the data
no2_subset.pivot(columns="location", values="value")
```
