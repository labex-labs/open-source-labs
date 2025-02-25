# Graficar los datos

Graficamos los datos refinados utilizando la función `tricontour` de Matplotlib.

```python
# Opciones gráficas para el trazado de contornos
niveles = np.arange(0., 1., 0.025)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_title("Filtrado de una malla de Delaunay\n"
             "(aplicación al trazado de contornos de alta resolución)")

# trazado de los contornos de los datos refinados (computados):
ax.tricontour(tri_refi, z_test_refi, niveles=niveles, cmap='Blues',
              linewidths=[2.0, 0.5, 1.0, 0.5])

plt.show()
```
