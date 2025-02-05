# 检测缺失值

接下来，我们将使用 `isna` 和 `notna` 函数来检测缺失值。

```python
# Use isna and notna to detect missing values
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```
