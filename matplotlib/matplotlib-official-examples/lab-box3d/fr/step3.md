# Tracer des surfaces de contour

Tracez des surfaces de contour pour la boîte en utilisant la méthode `contourf` pour chaque surface. Utilisez des paramètres appropriés pour `zdir` et `offset`.

```python
kw = {
    'vmin': data.min(),
    'vmax': data.max(),
    'levels': np.linspace(data.min(), data.max(), 10),
}

# Créez une figure avec un axe 3D
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

# Tracez des surfaces de contour
_ = ax.contourf(
    X[:, :, 0], Y[:, :, 0], data[:, :, 0],
    zdir='z', offset=0, **kw
)
_ = ax.contourf(
    X[0, :, :], data[0, :, :], Z[0, :, :],
    zdir='y', offset=0, **kw
)
C = ax.contourf(
    data[:, -1, :], Y[:, -1, :], Z[:, -1, :],
    zdir='x', offset=X.max(), **kw
)
```
