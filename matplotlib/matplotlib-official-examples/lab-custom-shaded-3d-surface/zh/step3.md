# 自定义山体阴影

在这一步中，我们将通过覆盖内置的阴影设置并传入从“shade”计算出的阴影表面的 RGB 颜色来自定义山体阴影。

```python
# 设置绘图
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# 要使用自定义山体阴影模式，请覆盖内置的阴影设置，并传入从“shade”计算出的阴影表面的 rgb 颜色。
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
