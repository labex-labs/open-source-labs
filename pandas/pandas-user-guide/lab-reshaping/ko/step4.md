# 교차 집계 (Cross Tabulations)

교차 집계는 여러 변수 간의 관계를 정량적으로 분석하는 방법입니다.

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
