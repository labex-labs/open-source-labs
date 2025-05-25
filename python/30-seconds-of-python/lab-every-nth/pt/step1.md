# Cada elemento nth em uma lista

Escreva uma função `every_nth(lst, nth)` que recebe uma lista `lst` e um inteiro `nth` como argumentos e retorna uma nova lista contendo cada elemento `nth` da lista original.

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
