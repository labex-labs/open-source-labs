# 使用自定义框样式

一旦你实现并注册了自定义框样式，就可以在 `Axes.text` 中使用它。

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```
