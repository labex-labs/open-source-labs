# Настраиваем график

В этом шаге мы настроим 3D-график «стеги», изменив базовую линию с использованием параметра `bottom` и изменив формат с использованием параметров `linefmt`, `markerfmt` и `basefmt`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
