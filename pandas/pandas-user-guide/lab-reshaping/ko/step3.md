# 다중 집계 (Multiple Aggregations) 를 사용한 피벗 (Pivoting)

Pivot 에서 여러 집계를 수행할 수도 있습니다.

```python
# Pivot df with the mean and sum of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
