# Add a new column for the month of the measurement

Now, we want to add a new column to our DataFrame that contains only the month of each measurement. This can be achieved using the `dt` accessor.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
