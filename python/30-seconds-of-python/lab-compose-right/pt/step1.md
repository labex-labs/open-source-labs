# Composição de Funções Inversa

Escreva uma função `compose_right` que recebe uma ou mais funções como argumentos e retorna uma nova função que realiza a composição de funções da esquerda para a direita (left-to-right). A primeira função (mais à esquerda) pode aceitar um ou mais argumentos; as funções restantes devem ser unárias.

Sua implementação deve usar a função `reduce` do módulo `functools` para realizar a composição de funções da esquerda para a direita.

```python
from functools import reduce

def compose_right(*fns):
  # seu código aqui
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
