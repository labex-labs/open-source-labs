# Bifurcar Lista com Base em Função

Escreva uma função `bifurcate_by(lst, fn)` que recebe uma lista `lst` e uma função de filtragem `fn` como argumentos. A função deve dividir a lista em dois grupos com base no resultado da função de filtragem. Se a função de filtragem retornar um valor verdadeiro (truthy) para um elemento, ele deve ser adicionado ao primeiro grupo. Caso contrário, ele deve ser adicionado ao segundo grupo.

Sua função deve retornar uma lista de duas listas, onde a primeira lista contém todos os elementos para os quais a função de filtragem retornou um valor verdadeiro, e a segunda lista contém todos os elementos para os quais a função de filtragem retornou um valor falso (falsy).

Use uma compreensão de lista (list comprehension) para adicionar elementos aos grupos, com base no valor retornado por `fn` para cada elemento.

```python
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
