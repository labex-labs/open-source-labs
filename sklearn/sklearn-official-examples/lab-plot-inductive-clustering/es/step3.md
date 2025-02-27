# Generar nuevas muestras

En este paso, generaremos nuevas muestras y las graficaremos junto con el conjunto de datos original. Usaremos nuevamente la función `make_blobs` para generar 10 nuevas muestras.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
