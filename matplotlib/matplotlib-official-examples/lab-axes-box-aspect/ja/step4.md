# 画像の隣に通常のプロットを作成する

固定されたデータアスペクトと既定の`adjustable="box"`を持つ画像プロットを通常のプロットの隣に作成する場合、軸の高さが異なります。`set_box_aspect()`は、通常のプロットの軸に画像の寸法をボックスアスペクトとして使用させることで、この問題を簡単に解決します。この例はまた、固定されたボックスアスペクトと良好に相互作用する「制約付きレイアウト」を示しています。

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
