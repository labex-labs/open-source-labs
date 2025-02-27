# Cargar el conjunto de datos del Titanic

A continuación, cargaremos el conjunto de datos del Titanic para demostrar `set_output` con `compose.ColumnTransformer` y datos heterogéneos.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
