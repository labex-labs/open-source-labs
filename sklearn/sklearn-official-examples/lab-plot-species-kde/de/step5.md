# Das Datennetz vorbereiten

Wir werden das Datennetz für das Konturndiagramm einrichten. Dazu verwenden wir die Funktion `construct_grids`.

```python
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0
```
