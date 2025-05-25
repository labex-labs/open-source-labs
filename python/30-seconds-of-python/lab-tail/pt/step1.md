# Cauda da Lista (List Tail)

Escreva uma função `tail(lst)` que recebe uma lista como argumento e retorna todos os elementos da lista, exceto o primeiro. Se a lista contiver apenas um elemento, retorne a lista inteira.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
