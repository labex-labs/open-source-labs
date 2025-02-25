# Создать график

Теперь, когда у нас есть данные, мы можем создать рамочную модель. В этом примере мы будем использовать функцию `plot_wireframe()` для создания графика.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
