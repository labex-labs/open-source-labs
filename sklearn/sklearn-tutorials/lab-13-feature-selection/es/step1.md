# Eliminación de características con baja varianza

La clase `VarianceThreshold` en scikit-learn se puede utilizar para eliminar características con baja varianza. Las características con baja varianza generalmente no proporcionan mucha información para el modelo. Demonstraremos cómo utilizar `VarianceThreshold` para eliminar características con varianza cero.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Inicializa VarianceThreshold con un umbral del 80% de variabilidad
sel = VarianceThreshold(threshold=(.8 * (1 -.8)))

# Selecciona características con alta variabilidad
X_selected = sel.fit_transform(X)

print("Forma original de X:", X.shape)
print("Forma de X con características seleccionadas:", X_selected.shape)
print("Características seleccionadas:", sel.get_support(indices=True))
```

Este fragmento de código demuestra cómo utilizar `VarianceThreshold` para eliminar características con varianza cero de un conjunto de datos. La salida mostrará la forma original del conjunto de datos y la forma después de seleccionar características con alta variabilidad.
