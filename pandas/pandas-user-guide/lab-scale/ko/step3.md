# 효율적인 데이터 타입 사용

Pandas 의 기본 데이터 타입은 메모리 효율성이 가장 높지 않습니다. 이 단계에서는 더 큰 데이터 세트를 메모리에 저장하기 위해 더 효율적인 데이터 타입을 사용하는 방법을 보여줍니다.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convert 'name' column to 'category' type for efficiency
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Downcast numeric columns to their smallest types
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```
