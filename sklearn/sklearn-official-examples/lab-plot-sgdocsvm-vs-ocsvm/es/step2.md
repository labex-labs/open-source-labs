# Generar datos

Generaremos un conjunto de datos de ejemplo para este laboratorio. Generaremos 500 muestras de entrenamiento y 20 muestras de prueba. También generaremos 20 muestras anómalas.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# Generar datos de entrenamiento
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# Generar algunas observaciones novedosas regulares
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Generar algunas observaciones novedosas anómalas
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
