# 生成随机数据

我们将使用 `numpy.random.random()` 生成一个三维随机数据数组。我们将使用一个种子值来确保每次运行代码时生成相同的数据集。

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
