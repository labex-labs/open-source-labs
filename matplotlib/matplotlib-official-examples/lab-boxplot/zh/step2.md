# 生成数据

我们将生成一些随机数据用于示例。我们会使用 NumPy 函数`random.lognormal()`来生成均值为 1.5、标准差为 1.75 的对数正态分布数据。我们将生成 4 个变量的 37 个样本，并将它们存储在`data`变量中。我们还会为每个变量创建一个标签列表。

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
