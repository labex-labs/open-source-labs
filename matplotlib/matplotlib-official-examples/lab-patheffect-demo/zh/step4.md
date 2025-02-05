# 为图例添加阴影效果

我们可以使用 `withSimplePatchShadow` 路径效果为图例添加阴影效果。

```python
# 创建绘图并为图例添加阴影效果
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```
