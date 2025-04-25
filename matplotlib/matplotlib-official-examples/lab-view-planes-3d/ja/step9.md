# 中央のサブプロットにラベルを追加する

これが一次 3D ビュープレーンのプロットであることを示すために、中央のサブプロットにラベルを追加します。

```python
label ='mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
