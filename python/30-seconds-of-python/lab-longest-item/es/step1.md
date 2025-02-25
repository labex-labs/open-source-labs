# Elemento más largo

Escribe una función `longest_item(*args)` que tome cualquier número de objetos iterables o objetos con una propiedad `length` y devuelva el más largo. La función debe:

- Utilizar `max()` con `len()` como `key` para devolver el elemento con la mayor longitud.
- Si varios elementos tienen la misma longitud, se devolverá el primero.

```python
def longest_item(*args):
  return max(args, key = len)
```

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
