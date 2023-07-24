# Concatenating the Datasets

Next, we will combine the measurements of Nitrate and Particulate matter into a single table using the `concat` function.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
