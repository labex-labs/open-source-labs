# Generar datos de muestra

Utilizaremos la función `make_blobs` de la biblioteca scikit-learn para generar datos de muestra. Esta función genera cúmulos gaussianos isotrópicos para el agrupamiento. Generaremos 4000 muestras con 4 centros.

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
