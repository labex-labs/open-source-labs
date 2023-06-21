# Compute Nearest Neighbors Graph

In this step, we will compute the nearest neighbors graph using KNeighborsTransformer.

```python
# The transformer computes the nearest neighbors graph using the maximum number
# of neighbors necessary in the grid search. The classifier model filters the
# nearest neighbors graph as required by its own n_neighbors parameter.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
