# Componiendo una leyenda personalizada

En este paso, crearemos una leyenda personalizada utilizando objetos de Matplotlib. Primero, importamos la clase `Line2D` del módulo `matplotlib.lines`. A continuación, creamos una lista de objetos `Line2D` con atributos personalizados de color, ancho y etiqueta. Finalmente, trazamos los datos nuevamente utilizando la función `plot` y llamamos a `legend()` con las líneas personalizadas y las etiquetas correspondientes.

```python
# Importa la clase Line2D
from matplotlib.lines import Line2D

# Crea líneas personalizadas
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Traza los datos y genera la leyenda personalizada
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
