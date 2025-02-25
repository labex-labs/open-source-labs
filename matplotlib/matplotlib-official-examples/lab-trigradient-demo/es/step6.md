# Graficar la triangulación, los contornos de iso-potencial y el campo vectorial

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

Explicación:

- `fig` y `ax` son, respectivamente, los objetos de figura y ejes.
- `ax.set_aspect` establece la relación de aspecto de los ejes.
- `ax.use_sticky_edges` y `ax.margins` establecen los márgenes de los ejes.
- `ax.triplot` grafica la triangulación.
- `ax.tricontour` grafica los contornos de iso-potencial.
- `ax.quiver` grafica el campo vectorial.
- `ax.set_title` establece el título de la gráfica.
