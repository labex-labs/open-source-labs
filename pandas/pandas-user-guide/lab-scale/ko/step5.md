# 다른 라이브러리 사용

Dask 와 같은 다른 라이브러리는 메모리보다 큰 데이터 세트를 처리할 수 있습니다. Dask 는 pandas 와 유사한 API 를 제공하며 데이터를 병렬로 처리할 수 있습니다.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Compute value counts using Dask
ddf["name"].value_counts().compute()
```
