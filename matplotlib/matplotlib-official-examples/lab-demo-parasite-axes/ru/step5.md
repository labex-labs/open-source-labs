# Показываем правую ось y первой паразитной оси

Мы показываем правую ось y первой паразитной оси с помощью метода `par1.axis["right"].set_visible(True)`. Мы также устанавливаем `par1.axis["right"].major_ticklabels.set_visible(True)` и `par1.axis["right"].label.set_visible(True)`, чтобы показать деление на шкале и метку правой оси y.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
