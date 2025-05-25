# Criar Dados

Criaremos um array numpy `x` contendo 500 valores espaçados uniformemente entre 0 e 3π. Também criaremos outro array numpy `y` contendo o seno dos valores em `x`. Finalmente, criaremos um array numpy `dydx` contendo a primeira derivada de `y`.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
