# Configurar os dados

Geraremos dois conjuntos de dados com valores aleatórios usando a biblioteca NumPy. Um conjunto representará as coordenadas x e y, e o outro conjunto representará a coordenada z.

```python
def randrange(n, vmin, vmax):
    """
    Função auxiliar para criar um array de números aleatórios com forma (n, )
    com cada número distribuído Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
