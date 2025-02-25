# Определяем функцию для полигона под графиком

Далее определим функцию `polygon_under_graph(x, y)`, которая строит список вершин, определяющий полигон, заполняющий пространство под линией графика (x, y). Эта функция предполагает, что x упорядочен по возрастанию.

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
