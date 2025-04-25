# 创建绘图

我们创建一个 4x3 的绘图网格，以展示具有不同混合模式和垂直夸张效果的山体阴影图。我们首先在第一行展示山体阴影强度图像，然后在其余行放置具有不同混合模式的山体阴影图。我们使用一个 for 循环来遍历不同的垂直夸张值和混合模式。

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay','soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
