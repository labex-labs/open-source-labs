# 演示 2 - 共享颜色条

我们将使用以下代码创建一个包含 3 张图像且带有共享颜色条的网格：

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# 由于 cbar_mode="single"，所有轴的 cax 属性是相同的。
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- 我们使用 `ImageGrid` 创建一个包含 3 张图像的网格。
- 我们将 `cbar_mode` 设置为 "single" 以添加一个共享颜色条。
- 我们将 `share_all` 参数设置为 True，以便在所有图像之间共享 x 轴和 y 轴。
- 我们将 `cbar_location` 参数设置为 "right"，以便将颜色条定位在右侧。
- 我们为第一张图像设置 `xticks` 和 `yticks`。
- 我们遍历每张图像，并使用 `imshow` 将图像添加到轴上。
- 我们设置 `clim` 参数以确保所有图像使用相同的颜色刻度。
- 我们使用 `ax.cax.colorbar` 为轴添加一个共享颜色条。
- 我们使用 `add_inner_title` 为每张图像添加一个标题。
