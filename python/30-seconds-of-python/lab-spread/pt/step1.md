# Spread List (Lista Spread)

Escreva uma função chamada `spread(arg)` que recebe uma lista como argumento e retorna uma nova lista que contém todos os elementos da lista original, achatados (flattened). Se um elemento da lista original for uma lista em si, seus elementos devem ser adicionados à nova lista individualmente. A função não deve modificar a lista original.

Para implementar a função, você deve iterar sobre os elementos da lista original e usar o operador spread para adicionar os elementos à nova lista. Se um elemento for uma lista, você deve usar o método `extend()` para adicionar seus elementos à nova lista. Se um elemento não for uma lista, você deve usar o método `append()` para adicioná-lo à nova lista.

```python
def spread(arg):
  ret = []
  for i in arg:
    ret.extend(i) if isinstance(i, list) else ret.append(i)
  return ret
```

```python
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
