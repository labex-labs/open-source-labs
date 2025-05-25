# Achatar uma Lista (Flatten a List)

Escreva uma função Python chamada `flatten(lst)` que recebe uma lista de listas como argumento e retorna uma lista achatada. A função deve apenas achatar a lista uma vez, o que significa que quaisquer listas aninhadas dentro da lista original devem ser achatadas, mas quaisquer listas aninhadas dentro dessas listas aninhadas devem permanecer intactas.

Para resolver este problema, você pode usar uma compreensão de lista (list comprehension) para extrair cada valor de sub-listas em ordem.

```python
def flatten(lst):
  return [x for y in lst for x in y]
```

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
