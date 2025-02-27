# Cargar el conjunto de datos

En este paso, cargaremos el conjunto de datos del Titanic de OpenML utilizando `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
