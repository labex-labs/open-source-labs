# グラフの下のポリゴンを定義する関数

次に、`polygon_under_graph(x, y)` という関数を定義します。この関数は、(x, y) の折れ線グラフの下の領域を埋めるポリゴンを定義する頂点リストを構築します。この関数は、x が昇順であることを前提としています。

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
