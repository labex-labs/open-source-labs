# Configurar los datos

Generaremos dos conjuntos de datos con valores aleatorios utilizando la biblioteca NumPy. Un conjunto representará las coordenadas x e y, y el otro conjunto representará la coordenada z.

```python
def randrange(n, vmin, vmax):
    """
    Función auxiliar para crear una matriz de números aleatorios con forma (n, )
    con cada número distribuido Uniformemente(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
