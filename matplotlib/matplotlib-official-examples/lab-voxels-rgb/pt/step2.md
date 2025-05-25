# Definindo as Coordenadas e Cores

Em seguida, precisamos definir as coordenadas e as cores para o gráfico. Neste exemplo, usaremos a função `np.indices` para criar uma grade 17x17x17 de valores para as cores RGB.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

Também definiremos uma função `midpoints` para encontrar os pontos médios entre os valores na grade. Isso será usado posteriormente para criar a esfera.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
