# 创建等高线图像

在这一步中，你将使用 Matplotlib 的 `contour` 和 `contourf` 函数来创建等高线图像。

```python
# 提高上限以避免截断误差。
levels = np.arange(-2.0, 1.601, 0.4)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig, _axs = plt.subplots(nrows=2, ncols=2)
fig.subplots_adjust(hspace=0.3)
axs = _axs.flatten()

cset1 = axs[0].contourf(X, Y, Z, levels, norm=norm,
                        cmap=cmap.resampled(len(levels) - 1))
# 这不是必需的，但对于颜色映射表，我们只需要级别数减 1。为避免离散化误差，可使用此数字或一个大数字，如默认值（256）。

# 如果我们想要线条和填充区域，需要分别调用 contour；不要尝试更改 contourf 返回的集合中多边形的边缘颜色或边缘宽度。
# 使用上一次调用的 levels 输出以确保它们相同。

cset2 = axs[0].contour(X, Y, Z, cset1.levels, colors='k')

# 我们实际上不需要虚线等高线来表示负区域，所以将它们关闭。

for c in cset2.collections:
    c.set_linestyle('solid')

# 在这里单独调用 contour 比设置颜色和线宽数组更容易。
# 我们绘制一条粗绿色线作为零等高线。
# 将零级别指定为仅包含 0 的元组。

cset3 = axs[0].contour(X, Y, Z, (0,), colors='g', linewidths=2)
axs[0].set_title('填充等高线')
fig.colorbar(cset1, ax=axs[0])


axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
axs[1].contour(Z, levels, colors='k', origin='upper', extent=extent)
axs[1].set_title("图像，原点 'upper'")

axs[2].imshow(Z, origin='lower', extent=extent, cmap=cmap, norm=norm)
axs[2].contour(Z, levels, colors='k', origin='lower', extent=extent)
axs[2].set_title("图像，原点 'lower'")

# 在这里我们将使用“nearest”插值来显示实际的图像像素。
# 请注意，等高线不会延伸到框的边缘。
# 这是有意的。Z 值在每个图像像素的中心（以下子图中的每个颜色块）定义，所以绘制等高线的域不会超出这些像素中心。
im = axs[3].imshow(Z, interpolation='nearest', extent=extent,
                   cmap=cmap, norm=norm)
axs[3].contour(Z, levels, colors='k', origin='image', extent=extent)
ylim = axs[3].get_ylim()
axs[3].set_ylim(ylim[::-1])
axs[3].set_title("来自 rc 的原点，y 轴反转")
fig.colorbar(im, ax=axs[3])

fig.tight_layout()
plt.show()
```
