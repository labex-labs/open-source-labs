# Calculate the average NO2 concentration for each day of the week

We can now calculate the average NO2 concentration for each day of the week at each measurement location. This can be done using the `groupby` method.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
