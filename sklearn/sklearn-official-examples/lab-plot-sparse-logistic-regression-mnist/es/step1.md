# Importar bibliotecas

Comenzaremos importando las bibliotecas necesarias para este laboratorio. Usaremos la biblioteca scikit-learn para obtener el conjunto de datos, entrenar el modelo y evaluar el rendimiento del modelo.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
