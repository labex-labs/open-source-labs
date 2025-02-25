# Настройка JoinStyle

Мы можем установить `JoinStyle` линии с использованием метода `set_solid_joinstyle()` объекта `Line2D`. Мы создадим новый объект линии и установим стиль соединения на `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
