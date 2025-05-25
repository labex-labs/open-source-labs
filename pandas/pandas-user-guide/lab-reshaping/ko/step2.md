# 단일 집계 (Single Aggregations) 를 사용한 피벗 (Pivoting)

Pivot 은 Pandas 에서 데이터를 재구성하는 주요 방법 중 하나입니다. 데이터를 다른 관점에서 볼 수 있도록 데이터를 변환하는 방법을 제공합니다.

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
