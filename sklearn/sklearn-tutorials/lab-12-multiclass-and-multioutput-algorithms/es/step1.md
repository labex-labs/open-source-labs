# Clasificación multicategoría

#### Descripción del problema

La clasificación multicategoría es una tarea de clasificación con más de dos clases. Cada muestra se asigna a una sola clase.

#### Formato de destino

Una representación válida de objetivos multicategoría es un vector de una dimensión o de columna que contiene más de dos valores discretos.

#### Ejemplo

Vamos a usar el conjunto de datos Iris para demostrar la clasificación multicategoría:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Cargar el conjunto de datos Iris
X, y = datasets.load_iris(return_X_y=True)

# Ajustar un modelo de regresión logística usando OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Hacer predicciones
predictions = model.predict(X)
print(predictions)
```
