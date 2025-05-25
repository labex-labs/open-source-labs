# Obter Valor Aninhado

Escreva uma função `get(d, selectors)` que recebe um dicionário ou lista `d` e uma lista de seletores `selectors` como argumentos e retorna o valor da chave aninhada indicada pela lista de seletores fornecida. Se a chave não existir, retorne `None`.

Para implementar esta função, use `functools.reduce()` para iterar sobre a lista `selectors`. Aplique `operator.getitem()` para cada chave em `selectors`, recuperando o valor a ser usado como o iterador para a próxima iteração.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
