# Preparar la malla de datos

Configuraremos la malla de datos para el gráfico de contornos. Utilizaremos la función `construct_grids` para lograr esto.

```python
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0
```
