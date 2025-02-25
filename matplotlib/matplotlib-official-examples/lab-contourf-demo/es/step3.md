# Crear contorno relleno con niveles explícitos

Ahora, crearemos un diagrama de contorno relleno con niveles explícitos. Usaremos el método `contourf` con el parámetro `levels` establecido en una lista de valores para especificar los niveles de contorno. También estableceremos la paleta de colores en una lista de colores y el parámetro `extend` en `'both'` para mostrar valores fuera del rango de niveles.

```python
# Crear contorno relleno con niveles explícitos
fig, ax = plt.subplots()
niveles = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, niveles, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, niveles, colors=('k',),
                 linewidths=(3,), origin=origin)

# Agregar título, etiquetas de eje y barra de colores
ax.set_title('Contorno Relleno con Niveles Explícitos')
ax.set_xlabel('Etiqueta de X')
ax.set_ylabel('Etiqueta de Y')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Etiqueta de Z')

# Mostrar el gráfico
plt.show()
```
