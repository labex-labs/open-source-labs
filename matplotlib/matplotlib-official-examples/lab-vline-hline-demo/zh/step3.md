# 给数据添加噪声

在这一步中，我们将给数据添加一些噪声，使其更接近实际情况。我们将使用 NumPy 的`normal`函数来生成均值为 0.0、标准差为 0.3 的随机数。

```python
# 给数据添加噪声
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
