# Создание второго подграфика

Во втором подграфике мы будем использовать `axisartist.axislines.AxesZero` для автоматического создания осей xzero и yzero. Мы сделаем другие ребра (spines) невидимыми и установим ось xzero видимой.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
