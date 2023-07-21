# Create Data

We need to create the `X` and `Y` coordinates using the `np.meshgrid()` function. Then, we create the `U` and `V` arrays that represent the vector fields.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
