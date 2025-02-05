# Create a Meshgrid

The third step is to create a meshgrid using `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
