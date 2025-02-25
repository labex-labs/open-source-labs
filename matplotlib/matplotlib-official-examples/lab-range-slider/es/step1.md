# Generar una imagen falsa

Primero, generaremos una imagen falsa en escala de grises utilizando el módulo `random` de NumPy. Estableceremos la semilla para garantizar que los resultados sean reproducibles.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
