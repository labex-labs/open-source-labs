# Generar un conjunto de datos

Generamos un conjunto de datos de forma (300, 300) con 5 biclusters y ruido de 5 utilizando la función `make_biclusters`.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
