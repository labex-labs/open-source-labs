# Построение трехмерной поверхности

В этом шаге мы построим трехмерную поверхность с использованием тестовых данных и настроим внешний вид графика.

```python
# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Customize the appearance of the plot
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
