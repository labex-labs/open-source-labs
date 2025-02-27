# Preparar los datos

Comenzamos definiendo una función que pretendemos aproximar y preparando para graficarla.

```python
def f(x):
    """Función a aproximar por interpolación polinómica."""
    return x * np.sin(x)

# rango completo que queremos graficar
x_plot = np.linspace(-1, 11, 100)

# Para hacerlo interesante, solo damos un subconjunto pequeño de puntos para entrenar.
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# crear versiones de 2D-array de estas matrices para alimentar a los transformadores
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```
