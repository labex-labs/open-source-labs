# Задаем пределы и отображаем сетку

В этом шаге мы зададим пределы для осей и отобразим сетку. Для установки соотношения сторон осей мы будем использовать `set_aspect()`, а для отображения сетки - `grid()`.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
