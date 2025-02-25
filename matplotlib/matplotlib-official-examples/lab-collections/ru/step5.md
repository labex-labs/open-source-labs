# Создать PolyCollection с использованием смещений

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

Пятым шагом является создание PolyCollection с использованием смещений. Мы будем использовать PolyCollection для заливки кривых цветами. Также мы будем использовать offset_transform для установки позиций кривых.
