# Create a New Column

We'll create a new column, "london_mg_per_cubic", by multiplying the "station_london" column by a conversion factor.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
