# Componiendo una leyenda personalizada con diferentes objetos de Matplotlib

En este paso, crearemos una leyenda personalizada utilizando diferentes objetos de Matplotlib, incluyendo `Line2D` y `Patch`. Primero, importamos la clase `Patch` del módulo `matplotlib.patches`. A continuación, creamos una lista de objetos `Line2D` y `Patch` con atributos personalizados. Finalmente, llamamos a `legend()` con los objetos personalizados y las etiquetas correspondientes.

```python
# Importa las clases Line2D y Patch
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Crea los elementos de la leyenda
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Linea'),
                   Line2D([0], [0], marker='o', color='w', label='Dispersión',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='naranja', edgecolor='r',
                         label='Parche de color')]

# Traza los datos y genera la leyenda personalizada
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
