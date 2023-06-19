# Creating a mesh to plot in

Now, we will create a mesh to plot in. The mesh will be used to plot the predicted probabilities for each point on the mesh. We will also define the step size for the mesh.

```python
h = 0.02  # step size in the mesh

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```


