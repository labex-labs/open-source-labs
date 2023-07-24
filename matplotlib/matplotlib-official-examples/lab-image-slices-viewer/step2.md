# Create the data

We will create 3D data using NumPy's `ogrid` function.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
