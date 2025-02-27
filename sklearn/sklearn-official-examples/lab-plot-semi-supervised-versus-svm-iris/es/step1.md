# Cargar el conjunto de datos Iris y dividir los datos

Cargaremos el conjunto de datos Iris, que es un conjunto de datos ampliamente utilizado en el aprendizaje automático para tareas de clasificación. El conjunto de datos contiene 150 muestras de flores de Iris, con cuatro características para cada muestra: longitud del sépalo, ancho del sépalo, longitud del pétalo y ancho del pétalo. Dividiremos el conjunto de datos en características de entrada y etiquetas de destino.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()

# Dividir el conjunto de datos en características de entrada y etiquetas de destino
X = iris.data[:, :2] # Solo usaremos las dos primeras características para fines de visualización
y = iris.target
```
