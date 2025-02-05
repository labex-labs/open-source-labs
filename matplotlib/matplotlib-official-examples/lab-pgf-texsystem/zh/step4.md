# 向图表添加文本

你可以使用 `ax.text()` 函数向图表添加文本。在本示例中，我们将添加具有不同字体族的文本。

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```
