# Use Chunking

Chunking is a method to split a large problem into smaller problems that can be solved independently. As long as each chunk fits in memory, you can work with datasets that are much larger than memory.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
