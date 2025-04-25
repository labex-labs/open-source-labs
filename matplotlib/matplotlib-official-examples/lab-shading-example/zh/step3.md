# 创建阴影浮雕图

现在我们将使用 `LightSource` 类创建阴影浮雕图。我们将创建两个子图，一个是带有颜色映射数据的，另一个是带有光照强度的。

```python
# 从西北方向照亮场景
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='颜色映射数据')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='光照强度')
```

我们将再创建两个子图，一个将 `blend_mode` 设置为“hsv”，另一个设置为“overlay”。

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='混合模式："hsv"（默认）')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='混合模式："overlay"')
```
