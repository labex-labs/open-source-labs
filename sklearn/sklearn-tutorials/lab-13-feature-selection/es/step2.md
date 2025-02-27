# Selección de características univariadas

La selección de características univariadas funciona seleccionando las mejores características basadas en pruebas estadísticas univariadas. En scikit-learn, hay varias clases que implementan la selección de características univariadas:

- `SelectKBest`: selecciona las k mejores características con la puntuación más alta
- `SelectPercentile`: selecciona un porcentaje especificado por el usuario de las características con la puntuación más alta
- `SelectFpr`: selecciona características basadas en la tasa de falsos positivos
- `SelectFdr`: selecciona características basadas en la tasa de descubrimiento falso
- `SelectFwe`: selecciona características basadas en el error global familiar
- `GenericUnivariateSelect`: permite la selección con una estrategia configurable

A continuación, se muestra un ejemplo de cómo utilizar `SelectKBest` para seleccionar las dos mejores características del conjunto de datos Iris:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Carga el conjunto de datos Iris
X, y = load_iris(return_X_y=True)

# Inicializa SelectKBest con la función de puntuación f_classif y k = 2
selector = SelectKBest(f_classif, k=2)

# Selecciona las mejores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X con características seleccionadas:", X_selected.shape)
print("Características seleccionadas:", selector.get_support(indices=True))
```

En este ejemplo, utilizamos la función de puntuación `f_classif` y seleccionamos las dos mejores características del conjunto de datos Iris. La salida mostrará la forma original del conjunto de datos y la forma después de seleccionar las mejores características.
