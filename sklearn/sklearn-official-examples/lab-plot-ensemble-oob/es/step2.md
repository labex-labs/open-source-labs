# Generar un conjunto de datos de clasificación binaria

A continuación, generaremos un conjunto de datos de clasificación binaria utilizando la función `make_classification` proporcionada por scikit-learn. Esta función nos permite especificar el número de muestras, características, clusters por clase y características informativas. Utilizaremos un valor fijo de estado aleatorio para garantizar la reproducibilidad.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
