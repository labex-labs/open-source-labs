# 합의 점수 계산

`consensus_score()` 함수를 사용하여 바이클러스터의 합의 점수를 계산합니다.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
