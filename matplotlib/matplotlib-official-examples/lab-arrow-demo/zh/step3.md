# 自定义箭头图

第三步是自定义箭头图。我们可以使用 `display` 参数来更改要显示的箭头属性。我们还可以使用 `shape` 参数来更改箭头的形状。我们可以分别使用 `max_arrow_width` 和 `arrow_sep` 参数来调整箭头的宽度和间距。我们可以使用 `alpha` 参数来更改箭头的透明度。我们还可以使用 `labelcolor` 参数来更改标签的颜色。

```python
# 绘制带有自定义设置的箭头图
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
