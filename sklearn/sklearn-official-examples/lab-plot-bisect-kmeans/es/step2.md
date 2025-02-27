# Generar datos de muestra

En este paso, generaremos datos de muestra utilizando la función `make_blobs()` de scikit-learn. Generaremos 10000 muestras con 2 centros.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
