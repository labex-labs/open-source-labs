# Almacenar en caché el gráfico de vecinos más cercanos

En este paso, almacenaremos en caché el gráfico de vecinos más cercanos entre múltiples ajustes de KNeighborsClassifier utilizando la propiedad de almacenamiento en caché de las tuberías.

```python
# Tenga en cuenta que le damos a `memory` un directorio para almacenar en caché el cálculo del gráfico
# que se utilizará varias veces al ajustar los hiperparámetros del
# clasificador.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
