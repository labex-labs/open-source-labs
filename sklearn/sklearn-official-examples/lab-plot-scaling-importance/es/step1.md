# Cargar y preparar los datos

Cargaremos el conjunto de datos de vinos de scikit-learn y lo dividiremos en conjuntos de entrenamiento y prueba. También escalaremos las características en el conjunto de entrenamiento utilizando el StandardScaler del módulo de preprocesamiento de scikit-learn.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```
