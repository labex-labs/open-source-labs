# Creando la gráfica de superficie 3D

Ahora podemos crear la gráfica de superficie 3D. Comenzamos creando una figura y agregando un subgráfico con el argumento `proyección='3d'`. Luego, utilizamos la función `plot_superficie()` para representar la superficie con los datos que creamos en el paso anterior.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
