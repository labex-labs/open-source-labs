# Agregando una línea para delimitar las regiones enmascaradas

Finalmente, agregamos una línea para delimitar las regiones enmascaradas. Creamos una matriz de valores de theta y trazamos un círculo con radio `r0` utilizando `np.cos(theta)` y `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
