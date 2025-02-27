# Generar datos

Generaremos datos de muestra utilizando la función `make_blobs` de la biblioteca `sklearn.datasets`. Esta función genera manchas gaussianas isotrópicas para el clustering.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # Para reproducibilidad
```
