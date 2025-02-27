# Cargar y preprocesar los datos

Comenzaremos cargando el conjunto de datos de dígitos manuscritos de scikit-learn y dividiéndolo en conjuntos de entrenamiento y prueba. También escalaremos los datos para que tengan media cero y varianza unitaria.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos de dígitos
X, y = datasets.load_digits(return_X_y=True)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos para que tengan media cero y varianza unitaria
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
