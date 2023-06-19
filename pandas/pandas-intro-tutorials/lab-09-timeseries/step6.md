# Resample time series data

The `resample` method is a powerful way to change the frequency of time series data. Here, we will aggregate the current hourly time series data to the monthly maximum value at each measurement station.

```python
# resample time series data
monthly_max = air_quality.resample("M").max()
```
