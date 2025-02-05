# 创建一个随机数据集

接下来，我们将创建一个随机数据集用于回归。我们将使用`numpy`创建一组600个介于 -100和100之间的x值，并根据x值的正弦和余弦计算出相应的y值，再加上一些随机噪声。

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
