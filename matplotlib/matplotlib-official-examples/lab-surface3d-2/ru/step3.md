# Создание трехмерной поверхностной диаграммы

Теперь мы можем создать трехмерную поверхностную диаграмму. Мы начинаем с создания фигуры и добавления подграфика с аргументом `projection='3d'`. Затем мы используем функцию `plot_surface()` для построения поверхности с использованием данных, созданных на предыдущем шаге.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
