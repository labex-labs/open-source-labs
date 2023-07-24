# Create a Mesh

We create a mesh in the space of parameterization variables `u` and `v`. This is done using the `np.meshgrid()` function to create a grid of `u` and `v` points.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
