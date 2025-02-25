# Crear un gráfico de contorno 3D

Crearemos un gráfico de contorno 3D utilizando la triangulación creada y las coordenadas z. También personalizaremos el ángulo de vista para que sea más fácil de entender el gráfico.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
