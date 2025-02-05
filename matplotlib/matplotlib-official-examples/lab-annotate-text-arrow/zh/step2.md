# 向图表添加文本注释

接下来，我们将使用 `ax.text()` 函数向图表添加文本注释。我们将创建两个注释，一个用于“样本 A”，另一个用于“样本 B”。

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
