# Создать RegularPolyCollection с использованием смещений

```python
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
col.set_color(colors)

ax3.add_collection(col, autolim=True)
ax3.autoscale_view()

ax3.set_title('RegularPolyCollection using offsets')
```

Шестым шагом является создание RegularPolyCollection с использованием смещений. Мы будем использовать RegularPolyCollection для создания правильных многоугольников с смещениями. Также мы будем использовать offset_transform для установки позиций многоугольников.
