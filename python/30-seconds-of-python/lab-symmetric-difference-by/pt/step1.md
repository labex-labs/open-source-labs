# Diferença Simétrica Baseada em Função

Escreva uma função `symmetric_difference_by(a, b, fn)` que recebe duas listas `a` e `b`, e uma função `fn`. A função deve retornar uma nova lista contendo todos os elementos que estão em qualquer uma das listas originais, mas não em ambas, após aplicar a função fornecida a cada elemento de ambas as listas.

Para resolver este problema, você pode seguir estes passos:

1.  Crie um `set` aplicando `fn` a cada elemento em cada lista.
2.  Use uma list comprehension em combinação com `fn` em cada uma delas para manter apenas os valores que não estão contidos no conjunto (set) criado anteriormente da outra.
3.  Concatene as duas listas obtidas no passo 2.

A função deve ter os seguintes parâmetros:

- `a`: uma lista de elementos
- `b`: uma lista de elementos
- `fn`: uma função que recebe um elemento e retorna um novo valor

A função deve retornar uma nova lista contendo todos os elementos que estão em qualquer uma das listas originais, mas não em ambas, após aplicar a função fornecida a cada elemento de ambas as listas.

```python
def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

```python
from math import floor

symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2, 3.4]
```
