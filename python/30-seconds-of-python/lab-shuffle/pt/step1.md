# Embaralhar Lista

Escreva uma função `shuffle(lst)` que recebe uma lista como entrada e retorna uma nova lista com os mesmos itens em uma ordem aleatória. Sua função deve usar o algoritmo Fisher-Yates para embaralhar os itens na lista.

O algoritmo Fisher-Yates funciona da seguinte forma:

1. Comece com o último item da lista.
2. Gere um índice aleatório entre 0 e o índice atual.
3. Troque o item no índice atual com o item no índice aleatório.
4. Vá para o próximo item na lista e repita os passos 2-3 até que todos os itens tenham sido embaralhados.

Sua função não deve modificar a lista original. Em vez disso, ela deve criar uma nova lista com os itens embaralhados.

Você pode assumir que a lista de entrada conterá pelo menos um item.

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
