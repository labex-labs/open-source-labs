# 计算一致性分数

我们使用 `consensus_score()` 函数来计算双聚类的一致性分数。

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
