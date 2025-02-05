# 自定义阴影图案

我们可以通过将阴影图案列表传递给 `pie()` 函数的 `hatch` 参数来自定义切片的阴影图案。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
