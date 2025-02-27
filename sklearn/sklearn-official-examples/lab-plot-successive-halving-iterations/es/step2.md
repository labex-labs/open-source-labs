# Cargando el conjunto de datos

La función `make_classification` del módulo `sklearn.datasets` se utiliza para generar un conjunto de datos de clasificación. El conjunto de datos contiene 400 muestras con 12 características. El código para cargar el conjunto de datos es el siguiente:

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
