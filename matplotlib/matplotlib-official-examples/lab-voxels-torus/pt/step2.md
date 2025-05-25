# Definir a Função de Pontos Médios

Em seguida, definimos uma função `midpoints` para calcular os pontos médios de um array de coordenadas. Esta função será usada posteriormente para calcular os pontos médios de `r`, `theta` e `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
