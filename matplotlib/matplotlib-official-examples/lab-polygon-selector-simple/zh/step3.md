# 交互式创建多边形

要交互式地创建多边形，我们需要创建一个 `Figure` 对象和一个 `Axes` 对象。然后，我们可以创建一个 `PolygonSelector` 对象，并通过在绘图上单击来向其添加顶点。我们还可以使用 `shift` 和 `ctrl` 键来移动顶点。

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("点击图形以创建多边形。")
print("按 'esc' 键开始绘制新的多边形。")
print("尝试按住'shift' 键以移动所有顶点。")
print("尝试按住 'ctrl' 键以移动单个顶点。")

plt.show()
```
