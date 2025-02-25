# Построим поверхность

В этом шаге мы построим поверхность с использованием функции `plot_surface()` библиотеки Matplotlib. Мы используем цветовую карту `YlGnBu_r` для настройки цвета поверхности.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
