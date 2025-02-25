# Personalizando las marcas y las etiquetas

Personalizaremos las marcas y las etiquetas de los ejes utilizando el método `ax1.tick_params()`. Estableceremos el color, la rotación y el tamaño de la etiqueta del eje x, y el color, el tamaño y el ancho de las marcas del eje y.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
