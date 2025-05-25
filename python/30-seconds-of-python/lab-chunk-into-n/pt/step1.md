# Dividir Lista em N Partes

Escreva uma função Python chamada `chunk_into_n(lst, n)` que recebe uma lista `lst` e um inteiro `n` como entrada e retorna uma lista de `n` listas menores, cada uma contendo um número igual de elementos da lista original. Se a lista original não puder ser dividida uniformemente em `n` listas menores, a parte final deve conter os elementos restantes.

Para resolver este problema, você pode seguir estes passos:

1.  Calcule o tamanho de cada parte dividindo o comprimento da lista original por `n` e arredondando para cima para o inteiro mais próximo usando a função `math.ceil()`.
2.  Crie uma nova lista de tamanho `n` usando as funções `list()` e `range()`.
3.  Use a função `map()` para mapear cada elemento da nova lista para uma parte da lista original com o comprimento de `size`.
4.  Retorne a lista de listas menores.

Sua função deve ter a seguinte assinatura:

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
