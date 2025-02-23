# Especificar puntos de texto y puntos de anotación

Debes especificar un punto de anotación `xy=(x, y)` para anotar ese punto. Además, puedes especificar un punto de texto `xytext=(x, y)` para la ubicación del texto de esta anotación. Opcionalmente, puedes especificar el sistema de coordenadas de `xy` y `xytext` con una de las siguientes cadenas para `xycoords` y `textcoords` (el valor predeterminado es 'data'):

- 'puntos de figura' : puntos a partir de la esquina inferior izquierda de la figura
- 'píxeles de figura' : píxeles a partir de la esquina inferior izquierda de la figura
- 'fracción de figura' : (0, 0) es la esquina inferior izquierda de la figura y (1, 1) es la esquina superior derecha
- 'puntos de eje' : puntos a partir de la esquina inferior izquierda del eje
- 'píxeles de eje' : píxeles a partir de la esquina inferior izquierda del eje
- 'fracción de eje' : (0, 0) es la esquina inferior izquierda del eje y (1, 1) es la esquina superior derecha
- 'puntos de desplazamiento' : Especifica un desplazamiento (en puntos) a partir del valor xy
- 'píxeles de desplazamiento' : Especifica un desplazamiento (en píxeles) a partir del valor xy
- 'data' : utilizar el sistema de coordenadas de datos del eje

Nota: para los sistemas de coordenadas físicos (puntos o píxeles) el origen es el (inferior, izquierdo) de la figura o del eje.

Opcionalmente, puedes especificar propiedades de flecha que dibujan una flecha desde el texto hasta el punto anotado proporcionando un diccionario de propiedades de flecha. Las claves válidas son:

- `width`: el ancho de la flecha en puntos
- `frac`: la fracción de la longitud de la flecha ocupada por la punta
- `headwidth`: el ancho de la base de la punta de la flecha en puntos
- `shrink`: mueve la punta y la base un cierto porcentaje alejada del punto anotado y del texto
- `cualquier clave para matplotlib.patches.polygon` (por ejemplo, facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Crea nuestra figura y los datos que utilizaremos para la representación
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Dibuja una línea y agrega algunas anotaciones simples
line, = ax.plot(t, s)
ax.annotate('píxeles de figura',
            xy=(10, 10), xycoords='píxeles de figura')
ax.annotate('puntos de figura',
            xy=(107, 110), xycoords='puntos de figura',
            fontsize=12)
ax.annotate('fracción de figura',
            xy=(.025,.975), xycoords='fracción de figura',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# Los siguientes ejemplos muestran cómo se dibujan estas flechas.

ax.annotate('desplazamiento de punto a partir de datos',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='puntos de desplazamiento',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('fracción de eje',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='fracción de eje',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# También puedes utilizar puntos o píxeles negativos para especificar a partir de (derecha, arriba).
# Por ejemplo, (-10, 10) es 10 puntos a la izquierda del lado derecho del eje y 10
# puntos arriba del fondo

ax.annotate('desplazamiento de píxel a partir de fracción de eje',
            xy=(1, 0), xycoords='fracción de eje',
            xytext=(-20, 20), textcoords='píxeles de desplazamiento',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
