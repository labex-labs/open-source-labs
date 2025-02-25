# Добавляем подпись к центральному подграфику

Мы добавляем подпись к центральному подграфику, чтобы показать, что это график основных трехмерных плоскостей обзора.

```python
label ='mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
