# Importar las bibliotecas necesarias y definir constantes

Primero, necesitamos importar las bibliotecas necesarias y definir los colores y la constante de semilla aleatoria para generar el conjunto de datos de múltiples etiquetas.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # rojo
        "#0198E1",  # azul
        "#BF5FFF",  # púrpura
        "#FCD116",  # amarillo
        "#FF7216",  # naranja
        "#4DBD33",  # verde
        "#87421F",  # marrón
    ]
)

# Utilizar la misma semilla aleatoria para múltiples llamadas a make_multilabel_classification para
# asegurar las mismas distribuciones
RANDOM_SEED = np.random.randint(2**10)
```
