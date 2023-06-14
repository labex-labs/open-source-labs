# Convert the image into a graph with the value of the gradient on the edges

We will convert the image into a graph with the value of the gradient on the edges. The smaller beta is, the more independent the segmentation is of the actual image. For beta=1, the segmentation is close to a voronoi.

```python
# Convert the image into a graph with the value of the gradient on the
# edges.
graph = image.img_to_graph(rescaled_coins)

# Take a decreasing function of the gradient: an exponential
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```


