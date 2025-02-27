# Importar bibliotecas

Comenzaremos importando las bibliotecas necesarias para este laboratorio. Usaremos la biblioteca scikit-learn para generar el conjunto de datos y entrenar los modelos de regresión logística, y la biblioteca matplotlib para trazar el límite de decisión.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
