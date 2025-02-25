# Создайте график Matplotlib

В этом шаге мы создадим график Matplotlib, который будет отображать наши данные. Мы начнем с создания фигуры и добавления подграфика.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
