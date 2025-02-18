# チャンク分割を使用する

チャンク分割（Chunking）は、大きな問題を独立して解くことができる小さな問題に分割する方法です。各チャンクがメモリに収まる限り、メモリよりもはるかに大きいデータセットを扱うことができます。

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
