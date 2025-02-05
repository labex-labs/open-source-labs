# 绘制阴影

我们通过使用与原线条稍有偏移且为灰色的相同线条来为线条绘制阴影。我们调整阴影线条的颜色和z轴顺序，使其绘制在原始线条下方。我们还使用 `offset_copy()` 方法为阴影线条创建一个偏移变换。

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
