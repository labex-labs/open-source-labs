# Preparación de los datos

Primero, crearemos un gran conjunto de datos de 80.000 muestras y lo dividiremos en tres conjuntos:

- Un conjunto para entrenar los métodos de conjunto que luego se utilizarán como transformador de ingeniería de características
- Un conjunto para entrenar el modelo lineal
- Un conjunto para probar el modelo lineal.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
