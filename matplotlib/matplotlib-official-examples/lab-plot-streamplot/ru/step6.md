# Управление точками начала

В этом шаге мы создадим поточную диаграмму с контролируемыми точками начала. Параметр `start_points` принимает двумерный массив, представляющий точки начала линий потока.

```python
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])

strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='autumn', start_points=seed_points.T)
plt.colorbar(strm.lines)
plt.title('Controlling Starting Points')
plt.plot(seed_points[0], seed_points[1], 'bo')
plt.xlim(-w, w)
plt.ylim(-w, w)
plt.show()
```
