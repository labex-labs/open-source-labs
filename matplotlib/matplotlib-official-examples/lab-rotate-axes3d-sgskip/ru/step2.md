# Создание трехмерной диаграммы

Далее мы создадим трехмерную диаграмму с использованием функций `plt.figure()` и `fig.add_subplot()`. Также мы будем использовать функцию `ax.plot_wireframe()` для построения набора данных в виде рамочного изображения.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
