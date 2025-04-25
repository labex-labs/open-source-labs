# 创建异或（XOR）数据集

在这一步中，我们将使用 NumPy 创建一个异或数据集。我们将使用`logical_xor`函数根据输入特征创建标签。

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
