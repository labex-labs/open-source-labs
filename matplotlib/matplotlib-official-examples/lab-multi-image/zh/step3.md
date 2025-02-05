# 设置颜色比例并创建颜色条

现在，我们将为图像设置颜色比例，并创建一个颜色条来显示数值范围。我们将找到所有图像的最小值和最大值，并相应地对颜色比例进行归一化。

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
