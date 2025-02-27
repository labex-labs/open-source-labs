# Agregar ruido

En este paso, agregaremos algo de ruido a los datos generados para crear un conjunto de datos de entrenamiento más realista.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
