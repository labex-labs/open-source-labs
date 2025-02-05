# 映射到 `x`、`y`、`z` 点

我们将 `radius`、`angle` 对映射到 `x`、`y`、`z` 点。

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
