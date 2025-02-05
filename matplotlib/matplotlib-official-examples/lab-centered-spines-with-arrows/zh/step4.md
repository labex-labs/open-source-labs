# 隐藏不必要的脊柱线

你还想隐藏顶部和右侧的脊柱线，因为它们不需要。

```python
ax.spines[["top", "right"]].set_visible(False)
```
