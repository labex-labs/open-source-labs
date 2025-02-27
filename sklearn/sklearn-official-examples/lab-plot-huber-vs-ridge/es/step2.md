# Generar datos de ejemplo

Ahora generaremos un conjunto de datos de ejemplo utilizando la función make_regression de scikit-learn. Generaremos un conjunto de datos con 20 muestras, una característica y una semilla aleatoria de 0. También agregaremos algo de ruido al conjunto de datos.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
