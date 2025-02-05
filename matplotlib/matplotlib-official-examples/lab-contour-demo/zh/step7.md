# 使用颜色映射表指定等高线颜色

我们可以使用颜色映射表来指定等高线的颜色。

```python
fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', origin='lower',
               cmap=cm.gray, extent=(-3, 3, -2, 2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels, origin='lower', cmap='flag', extend='both',
                linewidths=2, extent=(-3, 3, -2, 2))

# 加粗零等高线。
CS.collections[6].set_linewidth(4)

ax.clabel(CS, levels[1::2],  # 每隔一个级别标注
          inline=True, fmt='%1.1f', fontsize=14)

# 为等高线制作一个颜色条
CB = fig.colorbar(CS, shrink=0.8)

ax.set_title('Lines with colorbar')

# 我们仍然也可以为图像添加一个颜色条。
CBI = fig.colorbar(im, orientation='horizontal', shrink=0.8)

# 这使得原来的颜色条看起来有点不协调，
# 所以让我们改进一下它的位置。

l, b, w, h = ax.get_position().bounds
ll, bb, ww, hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])
```
