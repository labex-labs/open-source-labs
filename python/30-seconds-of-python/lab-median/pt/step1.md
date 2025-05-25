# Mediana (Median)

Escreva uma função Python chamada `find_median` que recebe uma lista de números como argumento e retorna a mediana da lista. Sua função deve realizar as seguintes etapas:

1.  Ordenar os números da lista usando `list.sort()`.
2.  Encontrar a mediana, que é o elemento do meio da lista se o comprimento da lista for ímpar, ou a média dos dois elementos do meio se o comprimento da lista for par.
3.  Retornar a mediana.

Sua função não deve usar nenhuma biblioteca ou função Python embutida que resolva diretamente o problema.

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
