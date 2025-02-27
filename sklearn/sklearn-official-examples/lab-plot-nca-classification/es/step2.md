# Cargar y preparar los datos

A continuación, cargaremos y prepararemos los datos. Cargaremos el conjunto de datos Iris utilizando scikit-learn y seleccionaremos solo dos características. Luego dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# solo tomamos dos características. Podríamos evitar este feo
# rebanado utilizando un conjunto de datos bidimensional
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, estratificar=y, tamaño_prueba=0.7, estado_aleatorio=42
)
```
