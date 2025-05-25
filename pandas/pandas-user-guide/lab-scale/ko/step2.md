# 적은 양의 데이터 로드

모든 데이터를 로드하는 대신, 필요한 열만 로드할 수 있습니다. 여기서는 parquet 파일에서 적은 양의 데이터를 로드하는 두 가지 방법을 보여줍니다.

```python
# Option 1: Load all data then filter
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Load only the requested columns
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
