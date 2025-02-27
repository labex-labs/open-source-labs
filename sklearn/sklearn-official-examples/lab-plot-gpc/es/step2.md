# Generar datos

Generaremos datos utilizando NumPy. Generaremos 100 puntos de datos con una distribución uniforme entre 0 y 5. Estableceremos el umbral en 2.5 y generaremos las etiquetas utilizando una expresión booleana. Utilizaremos los primeros 50 puntos de datos como datos de entrenamiento y el resto como datos de prueba.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
