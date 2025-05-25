# Criar Dados Sintéticos

Nesta etapa, criaremos um conjunto de dados sintéticos consistindo em duas "corcovas" (humps), uma negativa e outra positiva, com a corcova positiva tendo uma amplitude oito vezes maior que a corcova negativa. Em seguida, aplicaremos `SymLogNorm` para visualizar os dados.

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn', 'shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
