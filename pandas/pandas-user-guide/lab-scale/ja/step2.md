# 必要なデータのみを読み込む

すべてのデータを読み込む代わりに、必要な列のみを読み込むことができます。ここでは、parquet ファイルから必要なデータのみを読み込む 2 つの方法を紹介します。

```python
# Option 1: Load all data then filter
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Load only the requested columns
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
