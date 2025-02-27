# Preparar los datos

En este paso, prepararemos los conjuntos de datos de clasificación sintéticos para la discretización de características. Utilizaremos la biblioteca scikit-learn para generar tres conjuntos de datos diferentes: lunas, círculos concéntricos y datos linealmente separables.

```python
h = 0.02  # tamaño del paso en la malla

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
