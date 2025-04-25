# 生成数据

我们将使用 NumPy 生成数据。我们将生成 100 个数据点，其在 0 到 5 之间均匀分布。我们将阈值设置为 2.5，并使用布尔表达式生成标签。我们将前 50 个数据点用作训练数据，其余的用作测试数据。

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
