# 陰影起伏図の作成

ここでは、`LightSource` クラスを使って陰影起伏図を作成します。2つのサブプロットを作成します。1つはカラーマップ付きのデータで、もう1つは照明強度です。

```python
# シーンを北西から照明する
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Colormapped Data')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Illumination Intensity')
```

さらに2つのサブプロットを作成します。1つは `blend_mode` を "hsv" に設定し、もう1つは "overlay" に設定します。

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Blend Mode: "hsv" (default)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Blend Mode: "overlay"')
```
