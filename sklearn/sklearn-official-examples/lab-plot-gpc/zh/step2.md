# 生成数据

我们将使用NumPy生成数据。我们将生成100个数据点，其在0到5之间均匀分布。我们将阈值设置为2.5，并使用布尔表达式生成标签。我们将前50个数据点用作训练数据，其余的用作测试数据。

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
