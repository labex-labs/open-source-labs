# 对样本进行评分

在拟合估计器之后，我们可以使用 `score_samples` 方法来计算样本在估计的密度函数下的对数似然。这将为我们提供一个衡量每个样本根据密度估计的可能性大小的指标。

```python
scores = kde.score_samples(X)
```
