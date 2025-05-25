# Definindo Coisas

Nomes devem sempre ser definidos antes de serem usados posteriormente.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Requires that `a` is defined

z = square(b) # Requires `square` and `b` to be defined
```

**A ordem é importante.** Quase sempre você coloca as definições de variáveis e funções perto do topo.
