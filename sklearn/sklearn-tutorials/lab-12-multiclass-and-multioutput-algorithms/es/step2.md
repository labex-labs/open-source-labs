# Clasificación multilabel

#### Descripción del problema

La clasificación multilabel es una tarea de clasificación en la que cada muestra puede ser asignada múltiples etiquetas. El número de etiquetas que puede tener cada muestra es mayor que dos.

#### Formato de destino

Una representación válida de objetivos multilabel es una matriz binaria, donde cada fila representa una muestra y cada columna representa una clase. Un valor de 1 indica la presencia de la etiqueta en la muestra, mientras que 0 o -1 indica su ausencia.

#### Ejemplo

Vamos a crear un problema de clasificación multilabel usando la función make_classification:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Generar un problema de clasificación multilabel
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Ajustar un clasificador de bosque aleatorio multi-salida
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Hacer predicciones
predictions = model.predict(X)
print(predictions)
```
