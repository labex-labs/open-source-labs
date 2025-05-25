# 청크 (Chunking) 사용

청크는 큰 문제를 독립적으로 해결할 수 있는 더 작은 문제로 분할하는 방법입니다. 각 청크가 메모리에 맞는 한, 메모리보다 훨씬 큰 데이터 세트로 작업할 수 있습니다.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```
