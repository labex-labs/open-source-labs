# Define the Polygon Under Graph Function

Next, we define a function `polygon_under_graph(x, y)` which constructs the vertex list that defines the polygon filling the space under the (x, y) line graph. This function assumes that x is in ascending order.

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
