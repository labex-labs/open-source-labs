# Bifurcar Lista (Bifurcate List)

Escreva uma função `bifurcate(lst, filter)` que recebe uma lista `lst` e um filtro `filter` como entrada e retorna uma lista de duas listas. A primeira lista deve conter os elementos de `lst` que passam no filtro, e a segunda lista deve conter os elementos que não passam.

Para implementar esta função, você pode usar uma compreensão de lista (list comprehension) e a função `zip()`. A função `zip()` recebe duas ou mais listas como entrada e retorna uma lista de tuplas, onde cada tupla contém os elementos correspondentes de cada lista. Por exemplo, `zip([1, 2, 3], [4, 5, 6])` retorna `[(1, 4), (2, 5), (3, 6)]`.

Você pode usar esta função para iterar sobre `lst` e `filter` simultaneamente e adicionar os elementos à lista apropriada com base em se eles passam no filtro ou não.

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
