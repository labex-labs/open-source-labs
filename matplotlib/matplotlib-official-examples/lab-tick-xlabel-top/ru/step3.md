# Перемещение меток делений по оси x вверх

Для перемещения меток делений по оси x в верхнюю часть графика мы воспользуемся функцией `tick_params()` и установим параметры `top` и `labeltop` в значение `True`, а параметры `bottom` и `labelbottom` в значение `False`.

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
