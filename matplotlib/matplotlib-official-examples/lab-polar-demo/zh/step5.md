# 自定义图表

要自定义图表，你可以使用以下方法：

- `set_rmax` 用于设置 `r` 的最大值
- `set_rticks` 用于设置 `r` 的刻度值
- `set_rlabel_position` 用于设置径向标签的位置

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

你还可以使用 `set_title` 方法为图表添加标题。

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

最后，你可以使用 `grid` 方法为图表添加网格。

```python
ax.grid(True)
```
