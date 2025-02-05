# 创建带有多个组的散点图

我们可以通过遍历每个组并为该组创建一个散点图来创建带有多个组的散点图。我们分别使用 `c`、`s` 和 `alpha` 参数为每个组指定标记的颜色、大小和透明度。我们还将 `label` 参数设置为组名，该组名将用于图例中。

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
