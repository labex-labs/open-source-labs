# Construir el conjunto de datos

En este paso, crearemos un conjunto de datos de clasificación no linealmente separable compuesto por dos clusters de cuantiles gaussianos utilizando la función `make_gaussian_quantiles` del módulo `sklearn.datasets`. También concatenaremos los dos clusters y les asignaremos etiquetas.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
