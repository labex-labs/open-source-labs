# N Elementos Mínimos

Escreva uma função chamada `min_n(lst, n = 1)` que recebe uma lista `lst` e um inteiro opcional `n` (valor padrão de `1`). A função deve retornar uma nova lista contendo os `n` menores elementos da lista original `lst`. Se `n` não for fornecido, a função deve retornar uma lista contendo o menor elemento de `lst`.

Se `n` for maior ou igual ao comprimento de `lst`, a função deve retornar a lista original ordenada em ordem crescente.

Sua função deve realizar isso seguindo estas etapas:

1.  Use a função `sorted()` integrada para ordenar a lista em ordem crescente.
2.  Use a notação de fatiamento (slice notation) para obter o número especificado de elementos.
3.  Retorne a lista resultante.

```python
def min_n(lst, n = 1):
  return sorted(lst, reverse = False)[:n]
```

```python
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
