# Compor Funções

Escreva uma função chamada `compose(*fns)` que aceita uma ou mais funções como argumentos e retorna uma nova função que é o resultado da composição das funções de entrada da direita para a esquerda. A última função (mais à direita) pode aceitar um ou mais argumentos; as funções restantes devem ser unárias.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
