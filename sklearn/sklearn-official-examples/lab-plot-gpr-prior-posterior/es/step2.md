# Crear datos de entrenamiento

A continuación, creamos un conjunto de datos de entrenamiento que utilizaremos en las diferentes secciones.

```python
rng = np.random.RandomState(4)
X_train = rng.uniform(0, 5, 10).reshape(-1, 1)
y_train = np.sin((X_train[:, 0] - 2.5) ** 2)
n_samples = 5
```
