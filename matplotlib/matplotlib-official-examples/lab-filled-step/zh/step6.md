# 生成随机数据

我们将使用 `numpy.random.randn` 生成随机数据。我们将生成 4 组数据，每组有 12250 个点。

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
