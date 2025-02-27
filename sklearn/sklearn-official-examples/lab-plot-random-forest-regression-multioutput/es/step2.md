# Crear un conjunto de datos aleatorio

A continuación, crearemos un conjunto de datos aleatorio para utilizar en nuestra regresión. Utilizaremos `numpy` para crear un conjunto de 600 valores de x entre -100 y 100, y los valores correspondientes de y calculados a partir de la función seno y coseno de los valores de x más un poco de ruido aleatorio.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
