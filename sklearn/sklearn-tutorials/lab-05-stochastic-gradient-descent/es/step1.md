# Importar las bibliotecas necesarias

Primero, necesitamos importar las bibliotecas necesarias. Utilizaremos la biblioteca scikit-learn para el aprendizaje automático y el preprocesamiento de datos.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
