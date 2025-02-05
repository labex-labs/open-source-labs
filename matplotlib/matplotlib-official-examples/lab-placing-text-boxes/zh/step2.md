# 创建数据

在本示例中，我们将使用`numpy.random.randn()`创建一个随机数据集。

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
