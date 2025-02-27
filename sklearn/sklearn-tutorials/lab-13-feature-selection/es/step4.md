# Selección de características utilizando SelectFromModel

La clase `SelectFromModel` es un meta-transformador que se puede utilizar con cualquier estimador que asigna importancia a cada característica. Selecciona las características basadas en su importancia y elimina las características por debajo de un umbral especificado.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Carga el conjunto de datos Iris
X, y = load_iris(return_X_y=True)

# Inicializa RandomForestClassifier como el estimador
estimador = RandomForestClassifier()

# Inicializa SelectFromModel con el estimador y umbral de "media"
selector = SelectFromModel(estimador, threshold="mean")

# Selecciona las mejores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X con características seleccionadas:", X_selected.shape)
print("Características seleccionadas:", selector.get_support(indices=True))
```

En este ejemplo, utilizamos un clasificador de bosque aleatorio como el estimador y seleccionamos las características con una importancia mayor que la importancia media. La salida mostrará la forma original del conjunto de datos y la forma después de seleccionar las mejores características.
