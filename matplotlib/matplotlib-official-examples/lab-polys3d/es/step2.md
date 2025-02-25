# Definir la función del polígono debajo del gráfico

A continuación, definimos una función `polygon_under_graph(x, y)` que construye la lista de vértices que define el polígono que llena el espacio debajo del gráfico de líneas (x, y). Esta función asume que x está en orden ascendente.

```python
def polygon_under_graph(x, y):
    """
    Construye la lista de vértices que define el polígono que llena el espacio debajo
    del gráfico de líneas (x, y). Esto asume que x está en orden ascendente.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
