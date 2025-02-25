# Добавление легенды и цвета

Мы добавим легенду к графику и покрасим метки каждой оси в соответствии с цветом соответствующего набора данных с использованием функций `legend()` и `label.set_color()`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
