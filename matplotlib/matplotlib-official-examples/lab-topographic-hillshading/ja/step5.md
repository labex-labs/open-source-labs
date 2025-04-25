# プロットを作成する

異なるブレンドモードと垂直拡大率を持つヒルシェードプロットを表示するために、4x3 のプロットグリッドを作成します。最初に、1 行目にヒルシェード強度画像を表示し、その後、残りの行に異なるブレンドモードを持つヒルシェードプロットを配置します。異なる垂直拡大率の値とブレンドモードを for ループで反復処理します。

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
