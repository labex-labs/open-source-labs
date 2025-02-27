# Generar datos de entrenamiento

En este paso, generaremos algunos datos de entrenamiento a partir del agrupamiento. Usaremos la función `make_blobs` de scikit-learn para generar 5000 muestras con 3 clusters que tienen desviaciones estándar y centros diferentes.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
