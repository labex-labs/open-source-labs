# Criar o Eixo X Secundário

Criaremos o eixo x secundário e converteremos de frequência para período. Usaremos `one_over` como a função direta (forward function) e `inverse` como a função inversa (inverse function).

```python
def one_over(x):
    """Vectorized 1/x, treating x==0 manually"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# the function "1/x" is its own inverse
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('period [s]')
```
