# 打乱数据

为确保我们分析中的随机性，让我们打乱数据集中样本的顺序。

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
