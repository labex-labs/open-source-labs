# 色スケールの設定とカラーバーの作成

次に、画像の色スケールを設定し、値の範囲を示すカラーバーを作成します。すべての画像の最小値と最大値を見つけ、それに応じて色スケールを正規化します。

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
