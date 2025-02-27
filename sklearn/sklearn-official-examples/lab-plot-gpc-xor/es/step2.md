# Creando el conjunto de datos XOR

En este paso, crearemos un conjunto de datos XOR utilizando numpy. Utilizaremos la función logical_xor para crear las etiquetas basadas en las características de entrada.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
