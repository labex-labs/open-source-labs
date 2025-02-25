# Personalizar las propiedades de las marcas de los ejes y la cuadrícula

Podemos personalizar las propiedades de las marcas de los ejes y la cuadrícula utilizando las funciones `grid()` y `tick_params()`. En este ejemplo, cambiaremos el color y el tamaño de las etiquetas de las marcas y el ancho y el estilo de las líneas de la cuadrícula.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
