# 自定义颜色

我们可以通过将颜色列表传递给 `pie()` 函数的 `colors` 参数来自定义扇区的颜色。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```
