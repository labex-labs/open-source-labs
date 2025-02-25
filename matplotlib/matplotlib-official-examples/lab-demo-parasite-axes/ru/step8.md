# Добавляем легенду и цвета осей

Мы добавляем легенду к основной оси с помощью метода `host.legend()`. Мы также задаем цвет метки левой оси y основной оси, цвет метки правой оси y первой паразитной оси и цвет метки правой оси y второй паразитной оси, чтобы они соответствовали своим соответствующим линиям, с помощью методов `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())` и `par2.axis["right2"].label.set_color(p3.get_color())`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
