# Verificar se os Elementos da Lista são Idênticos

Escreva uma função `all_equal(lst)` que recebe uma lista como argumento e retorna `True` se todos os elementos na lista são idênticos, e `False` caso contrário.

Para resolver este problema, você pode usar os seguintes passos:

1. Use `set()` para eliminar elementos duplicados na lista.
2. Use `len()` para verificar se o comprimento do conjunto é `1`.
3. Se o comprimento do conjunto for `1`, retorne `True`. Caso contrário, retorne `False`.

```python
def all_equal(lst):
  return len(set(lst)) == 1
```

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
