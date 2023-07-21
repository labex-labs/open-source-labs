# Combining the Colors

We will now combine the RGB color components into a single array of shape `(17, 17, 17, 3)`.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
