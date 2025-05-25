# Deslocamento de Elementos da Lista

Escreva uma função `offset(lst, offset)` que recebe uma lista `lst` e um inteiro `offset` como argumentos e retorna uma nova lista com a quantidade especificada de elementos movidos para o final da lista. Se o `offset` for positivo, mova os primeiros `offset` elementos para o final da lista. Se o `offset` for negativo, mova os últimos `offset` elementos para o início da lista.

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
