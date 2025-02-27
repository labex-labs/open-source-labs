# Clasificación multicategoría-multi-salida

#### Descripción del problema

La clasificación multicategoría-multi-salida, también conocida como clasificación multitarea, predice múltiples propiedades no binarias para cada muestra. Cada propiedad puede tener más de dos clases.

#### Formato de destino

Una representación válida de objetivos multicategoría-multi-salida es una matriz densa, donde cada fila representa una muestra y cada columna representa una propiedad o clase diferente.

#### Ejemplo

Vamos a crear un problema de clasificación multicategoría-multi-salida usando la función make_classification:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Generar un problema de clasificación multicategoría-multi-salida
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Ajustar un clasificador de vectores de soporte multi-salida
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Hacer predicciones
predictions = model.predict(X)
print(predictions)
```
