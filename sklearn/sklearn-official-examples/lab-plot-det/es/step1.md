# Generar datos sintéticos

Usaremos la función `make_classification` de scikit-learn para generar datos sintéticos. Esta función genera un problema de clasificación aleatorio de n clases, con n_informative características informativas, n_redundant características redundantes y n_clusters_per_class clusters por clase. Generaremos 1000 muestras con 2 características informativas y un estado aleatorio de 1. Luego dividiremos los datos en conjuntos de entrenamiento y prueba con una proporción de 60/40.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
