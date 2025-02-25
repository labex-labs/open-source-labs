# Crear la representación de wireframe tridimensional

Crearemos una representación de wireframe tridimensional para el segundo subgráfico. Utilizaremos la función `get_test_data` de mpl_toolkits.mplot3d.axes3d para crear los datos del gráfico.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
