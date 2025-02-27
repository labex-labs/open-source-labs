# Generar el conjunto de datos

A continuación, generaremos un conjunto de datos que siga una curva sinusoidal ruidosa.

```python
# Parámetros
n_samples = 100

# Generar muestra aleatoria siguiendo una curva sinusoidal
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
