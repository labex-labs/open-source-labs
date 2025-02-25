# Определяем функцию обратного вызова выбора

Функция обратного вызова выбора будет вызываться каждый раз, когда пользователь выбирает прямоугольник или эллипс. Функция будет получать события нажатия и отпускания в качестве аргументов и выводить координаты прямоугольника или эллипса.

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
