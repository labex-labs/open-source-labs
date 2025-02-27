# Crear conjuntos de entrenamiento y prueba

Dividimos el conjunto de datos en un conjunto de entrenamiento con 1000 muestras y un conjunto de prueba con 100 muestras. Agregamos ruido gaussiano al conjunto de prueba y creamos dos copias de los datos originales; una con ruido y otra sin ruido.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
