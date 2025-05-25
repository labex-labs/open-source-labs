# Índice do Elemento Máximo

Escreva uma função `max_element_index(arr)` que recebe uma lista `arr` como argumento e retorna o índice do elemento com o valor máximo. Se houver múltiplos elementos com o valor máximo, retorne o índice da primeira ocorrência.

Para resolver este problema, você pode seguir estes passos:

1.  Use a função embutida `max()` para encontrar o valor máximo na lista.
2.  Use a função embutida `list.index()` para encontrar o índice da primeira ocorrência do valor máximo na lista.
3.  Retorne o índice.

```python
def max_element_index(arr):
  return arr.index(max(arr))
```

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```
