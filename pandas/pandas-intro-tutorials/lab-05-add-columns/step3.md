# Check the Ratio of Values in Two Columns

Next, we'll check the ratio of the values in the "station_paris" and "station_antwerp" columns and save the result in a new column.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
