# Cargar el conjunto de datos de diabetes

Comenzamos cargando el conjunto de datos de diabetes de scikit-learn y solo seleccionando una característica del conjunto de datos.

```python
import numpy as np
from sklearn import datasets

# Cargar el conjunto de datos de diabetes
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Utilizar solo una característica
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
