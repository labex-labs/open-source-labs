# Map to `x`, `y`, `z` Points

We map the `radius`, `angle` pairs to `x`, `y`, `z` points.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
