# Definir a Função Polígono Sob o Gráfico

Em seguida, definimos uma função `polygon_under_graph(x, y)` que constrói a lista de vértices que define o polígono preenchendo o espaço sob o gráfico de linhas (x, y). Esta função assume que x está em ordem crescente.

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
