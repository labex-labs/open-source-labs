# Cada elemento n-ésimo en una lista

Escribe una función `every_nth(lst, nth)` que tome una lista `lst` y un entero `nth` como argumentos y devuelva una nueva lista que contenga cada elemento `n`-ésimo de la lista original.

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
