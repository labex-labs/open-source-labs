# Создание вставленной оси

Создайте вставленную ось с помощью функции `zoomed_inset_axes`. Задайте уровень приближения и расположение вставленной оси внутри основного графика.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
