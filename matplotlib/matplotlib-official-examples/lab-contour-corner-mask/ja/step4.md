# プロットの作成

このステップでは、`contourf()`関数を使用してマスク付きコントーアプロットを作成します。この関数には、作成したいプロットの種類に応じて`corner_mask`引数を`True`または`False`に設定しながら、`x`、`y`、および`z`配列を渡します。

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
