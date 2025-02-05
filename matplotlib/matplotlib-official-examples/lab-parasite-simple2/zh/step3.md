# 创建图表

现在我们将使用`parasite_axes`模块中的`HostAxes`和`twin()`函数来创建图表。`HostAxes`用于创建主图表，而`twin()`用于创建次y轴。

```python
fig = plt.figure()

# 创建HostAxes对象
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# 使用变换后的坐标创建次y轴
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# 绘制数据
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# 设置轴标签
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# 隐藏次y轴上的刻度标签
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# 设置图表范围
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
