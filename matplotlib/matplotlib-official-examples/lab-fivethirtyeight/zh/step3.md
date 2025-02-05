# 为折线图创建数据

在这一步中，我们将为折线图创建数据。我们将使用 NumPy 的 `linspace` 函数创建一个在 0 到 10 之间均匀分布的值的数组。我们还将使用 NumPy 的 `random.randn` 函数生成一些随机噪声。

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
