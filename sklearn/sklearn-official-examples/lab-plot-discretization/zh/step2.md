# 创建数据集

在这一步中，我们将创建一个包含连续输入特征和连续输出特征的数据集。我们将使用 `numpy.random.RandomState()` 方法为输入特征生成随机数，并使用 `numpy.sin()` 方法生成输出特征。

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
