# Generar datos aleatorios

Generaremos una matriz tridimensional de datos aleatorios utilizando `numpy.random.random()`. Utilizaremos un valor de semilla para garantizar que se genere el mismo conjunto de datos cada vez que se ejecute el código.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
