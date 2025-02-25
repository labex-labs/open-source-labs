# Создаем фигуру и оси

Нам нужно создать фигуру и оси для штрих-кода. Мы установим размер фигуры в несколько раз больше количества данных и отключим все оси.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
