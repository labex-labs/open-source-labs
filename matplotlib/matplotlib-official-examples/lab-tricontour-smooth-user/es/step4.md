# Graficar la Triangulación y los contornos de iso-valor de alta resolución

En este paso, graficamos la Triangulación y los contornos de iso-valor de alta resolución utilizando `ax.triplot`, `ax.tricontourf` y `ax.tricontour`.

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.triplot(triang, lw=0.5, color='white')

levels = np.arange(0., 1., 0.025)
ax.tricontourf(tri_refi, z_test_refi, levels=levels, cmap='terrain')
ax.tricontour(tri_refi, z_test_refi, levels=levels,
              colors=['0.25', '0.5', '0.5', '0.5', '0.5'],
              linewidths=[1.0, 0.5, 0.5, 0.5, 0.5])

ax.set_title("High-resolution tricontouring")

plt.show()
```
