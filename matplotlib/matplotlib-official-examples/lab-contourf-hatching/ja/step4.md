# 凡例付きの無色のハッチ付きプロット

このステップでは、無色のハッチ付きのプロットを作成し、凡例を追加します。等高線を作成するために `contour` 関数を使用し、無色のハッチを指定するために `contourf` 関数を使用します。

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
