# Rotacionar Elementos da Lista

Escreva uma função `roll(lst, offset)` que recebe uma lista `lst` e um inteiro `offset`. A função deve mover a quantidade especificada de elementos para o início da lista. Se `offset` for positivo, os elementos devem ser movidos do final da lista para o início. Se `offset` for negativo, os elementos devem ser movidos do início da lista para o final.

Retorne a lista modificada.

```python
def roll(lst, offset):
  return lst[-offset:] + lst[:-offset]
```

```python
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
