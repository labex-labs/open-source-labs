# Grafica superficies de contorno

Grafica superficies de contorno para la caja utilizando el método `contourf` para cada superficie. Utiliza parámetros adecuados para `zdir` y `offset`.

```python
kw = {
    'vmin': data.min(),
    'vmax': data.max(),
    'levels': np.linspace(data.min(), data.max(), 10),
}

# Crea una figura con un eje 3D
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

# Grafica superficies de contorno
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
