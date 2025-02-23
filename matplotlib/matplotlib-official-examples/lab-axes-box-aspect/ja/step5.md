# 正方形の結合/マージナルプロット

結合データのプロットの隣にマージナル分布を表示したい場合があります。次のコードは、マージナル軸のボックスアスペクトがグリッドスペックの幅と高さの比率に等しい正方形のプロットを作成します。これにより、すべての軸が完全に整列し、グラフのサイズに関係なくなります。

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```
