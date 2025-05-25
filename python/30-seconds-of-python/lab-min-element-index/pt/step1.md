# Índice do elemento mínimo

Escreva uma função `min_element_index(arr)` que recebe uma lista de inteiros `arr` como argumento e retorna o índice do elemento com o valor mínimo na lista.

Para resolver este problema, você pode usar a função `min()` para obter o valor mínimo na lista e, em seguida, usar o método `list.index()` para retornar seu índice.

```python
def min_element_index(arr):
  return arr.index(min(arr))
```

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
