# Создать LineCollection с использованием смещений

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

Четвёртым шагом является создание LineCollection с использованием смещений. Мы будем использовать LineCollection для создания кривых с смещениями. Также мы будем использовать offset_transform для установки позиций кривых.
