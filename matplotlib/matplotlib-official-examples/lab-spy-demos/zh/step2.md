# 创建随机数组

接下来，我们将使用`numpy.random.randn`函数创建一个维度为(20, 20)的随机数组。我们还将把一些元素设置为零，以创建一个稀疏矩阵。

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
