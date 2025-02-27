# Importar bibliotecas y cargar el conjunto de datos

Comencemos importando las bibliotecas necesarias y cargando el conjunto de datos iris. Usaremos la función `load_iris` del módulo `sklearn.datasets` para cargar el conjunto de datos.

```python
from sklearn.datasets import load_iris

# Cargar el conjunto de datos iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Variable objetivo

print("Número de muestras:", X.shape[0])
print("Número de características:", X.shape[1])
print("Número de clases:", len(set(y)))
```
