# Load Less Data

Instead of loading all the data, we can load only the columns we need. Here, we demonstrate two methods to load less data from the parquet file.

```python
# Option 1: Load all data then filter
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Load only the requested columns
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
