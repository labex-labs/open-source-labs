# 创建一个随机数据集

我们将使用NumPy创建一个随机数据集，并给它添加一些噪声。

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
