# 创建图表

既然我们已经有了数据，就可以使用 Matplotlib 创建图表了。在本示例中，我们将使用 `plot()` 函数创建一个散点图。

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
