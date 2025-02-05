# 使用分块

分块是一种将大问题分解为可独立解决的小问题的方法。只要每个块能装入内存，你就可以处理比内存大得多的数据集。

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
