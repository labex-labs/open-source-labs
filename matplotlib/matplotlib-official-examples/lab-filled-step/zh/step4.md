# 设置固定区间的直方图函数

我们将使用 `numpy.histogram` 设置一个具有固定区间的直方图函数。我们将创建 20 个区间，范围从 -3 到 3。

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
