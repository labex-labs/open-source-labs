# Importar bibliotecas y definir la función

El primer paso es importar las bibliotecas necesarias y definir la función `make_arrow_graph()`. Esta función toma varios parámetros, como los ejes, los datos, el tamaño, la visualización, la forma, el ancho máximo de flecha, la separación de flechas, el alfa, la normalización de datos, el color del borde, el color de etiqueta y los argumentos clave palabra adicionales. Utiliza estos parámetros para crear un diagrama de flechas.

```python
# Importar bibliotecas
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Definir la función
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Crea un diagrama de flechas.

    Parámetros
    ----------
    ax
        Los ejes donde se dibuja el gráfico.
    data
        Diccionario con las probabilidades de las bases y las transiciones de pares.
    size
        Tamaño del gráfico, en pulgadas.
    display : {'length', 'width', 'alpha'}
        La propiedad de la flecha que se va a cambiar.
    shape : {'full', 'left', 'right'}
        Para flechas completas o semicirculares.
    max_arrow_width : float
        Ancho máximo de una flecha, en coordenadas de datos.
    arrow_sep : float
        Separación entre flechas de un par, en coordenadas de datos.
    alpha : float
        Opacidad máxima de las flechas.
    **kwargs
        Propiedades de `.FancyArrow`, por ejemplo *linewidth* o *edgecolor*.
    """

    # bloque de código
```
