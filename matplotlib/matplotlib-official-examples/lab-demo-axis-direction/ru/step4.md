# Изменение направления оси

Теперь мы создадим цикл, чтобы настроить четыре различных графика с плавающей осью в каждом из четырех основных направлений. В цикле мы будем использовать `add_floating_axis1()` и `add_floating_axis2()` для добавления плавающих осей и `set_axis_direction()` для настройки направления оси.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
