# Crear una matriz aleatoria

A continuación, crearemos una matriz aleatoria utilizando numpy. Utilizaremos el método `rand` para crear una matriz de 5x3 con valores aleatorios entre 0 y 1. También estableceremos una semilla aleatoria para garantizar la reproducibilidad de los resultados.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
