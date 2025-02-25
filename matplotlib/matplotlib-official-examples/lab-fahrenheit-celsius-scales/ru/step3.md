# Определяем функцию для обновления второй оси

Мы определим замыкание-функцию для регистрации в качестве обратного вызова для обновления второй оси в соответствии с первой осью.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Обновляет вторую ось в соответствии с первой осью.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
