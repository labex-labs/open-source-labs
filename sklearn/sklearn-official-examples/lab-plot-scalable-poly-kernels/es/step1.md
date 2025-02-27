# Cargar y Preparar los Datos

Primero cargaremos el conjunto de datos Covtype y lo transformaremos en un problema de clasificación binaria seleccionando solo una clase. Luego, dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba, y normalizaremos las características.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Cargar el conjunto de datos Covtype, seleccionando solo una clase
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# Dividir los datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Normalizar las características
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
