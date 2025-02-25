# `x`、`y`、`z` の点にマッピングする

`radius` と `angle` のペアを `x`、`y`、`z` の点にマッピングします。

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
