# Crear contorno relleno con niveles automáticos

A continuación, crearemos un diagrama de contorno relleno con niveles automáticos. Usaremos el método `contourf` con el parámetro `cmap` establecido en `plt.cm.bone` para especificar la paleta de colores. También agregaremos líneas de contorno con el método `contour` y pasaremos un subconjunto de los niveles de contorno utilizados para los contornos rellenos.

```python
# Crear contorno relleno con niveles automáticos
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Agregar título, etiquetas de eje y barra de colores
ax.set_title('Contorno Relleno con Niveles Automáticos')
ax.set_xlabel('Etiqueta de X')
ax.set_ylabel('Etiqueta de Y')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Etiqueta de Z')
cbar.add_lines(CS2)

# Mostrar el gráfico
plt.show()
```
