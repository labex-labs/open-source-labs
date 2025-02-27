# Conjunto de datos y modelo

Utilizaremos el conjunto de datos iris y un clasificador Linear SVC para diferenciar dos tipos de iris. Primero, importaremos las bibliotecas necesarias y cargaremos el conjunto de datos.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Luego, agregaremos características ruidosas al conjunto de datos y lo dividiremos en conjuntos de entrenamiento y prueba.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Finalmente, escalaremos los datos utilizando un StandardScaler y ajustaremos un clasificador Linear SVC a los datos de entrenamiento.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
