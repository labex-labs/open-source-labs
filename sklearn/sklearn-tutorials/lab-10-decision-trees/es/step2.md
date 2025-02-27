# Cargar el conjunto de datos

A continuación, cargaremos el conjunto de datos Iris. Este conjunto de datos contiene información sobre cuatro características de tres diferentes especies de flores Iris. Usaremos este conjunto de datos para entrenar nuestro clasificador de Árboles de Decisión.

```python
# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target
```
