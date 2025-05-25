# Testar se alguns elementos da lista são truthy (verdadeiros)

Escreva uma função `some(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve retornar `True` se a função `fn` retornar `True` para pelo menos um elemento na lista `lst`. Se nenhum elemento na lista satisfaz a condição, a função deve retornar `False`. Se nenhuma função for fornecida, a função deve usar a função identidade (que retorna o próprio elemento).

```python
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
