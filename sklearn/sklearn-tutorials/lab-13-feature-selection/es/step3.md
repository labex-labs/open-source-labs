# Eliminación recursiva de características

La eliminación recursiva de características (RFE, por sus siglas en inglés) es un método de selección de características que considera de manera recursiva conjuntos de características cada vez más reducidos para seleccionar las más importantes. Funciona entrenando un estimador externo con pesos asignados a las características y eliminando las menos importantes.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Carga el conjunto de datos Iris
X, y = load_iris(return_X_y=True)

# Inicializa SVC como el estimador externo
estimador = SVC(kernel="linear")

# Inicializa RFE con el estimador externo y selecciona 2 características
selector = RFE(estimador, n_features_to_select=2)

# Selecciona las mejores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X con características seleccionadas:", X_selected.shape)
print("Características seleccionadas:", selector.get_support(indices=True))
```

En este ejemplo, utilizamos un clasificador basado en vectores de soporte (SVC) como estimador externo y seleccionamos las dos mejores características del conjunto de datos Iris. La salida mostrará la forma original del conjunto de datos y la forma después de seleccionar las mejores características.
