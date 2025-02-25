# Добавление осей на фигуру

Мы добавим оси на фигуру с использованием функции `add_axes()` и передав позицию объекта `Divider`.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
