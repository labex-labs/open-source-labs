# Create a Graph

Create a graph capturing local connectivity. Larger number of neighbors will give more homogeneous clusters at the cost of computation time. A very large number of neighbors gives more evenly distributed cluster sizes but may not impose the local manifold structure of the data.

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
