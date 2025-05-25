# Fundir Listas

Escreva uma função chamada `merge(*args, fill_value=None)` que recebe duas ou mais listas como argumentos e retorna uma lista de listas. A função deve combinar elementos de cada uma das listas de entrada com base em suas posições. Se uma lista for menor que a lista mais longa, a função deve usar `fill_value` para os itens restantes. Se `fill_value` não for fornecido, ele deve ser definido como `None` por padrão.

Sua tarefa é implementar a função `merge()`.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
