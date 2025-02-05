# 对齐次刻度标签

最后，我们需要将次刻度标签对齐到主刻度之间的中心位置。我们可以使用 `get_xticklabels()` 函数，并将 `minor` 参数设置为 `True` 来获取次刻度标签。然后，我们可以遍历这些标签，并将水平对齐方式设置为 `'center'`。

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
