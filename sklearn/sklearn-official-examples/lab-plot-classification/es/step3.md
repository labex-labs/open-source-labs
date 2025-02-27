# Preparar los datos

Tomaremos solo las primeras dos características del conjunto de datos Iris, que son la longitud del sépalo y el ancho del sépalo. Luego dividiremos los datos en la matriz de características `X` y el vector objetivo `y`.

```python
X = iris.data[:, :2]
y = iris.target
```
