# 生成随机数据

我们将使用 `numpy.random.randn` 生成随机数据。我们将生成4组数据，每组有12250个点。

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
