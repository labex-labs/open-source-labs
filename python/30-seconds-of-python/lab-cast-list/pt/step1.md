# Converter para Lista

Escreva uma função `cast_list(val)` que recebe um valor como argumento e o retorna como uma lista. Se o valor já for uma lista, retorne-o como está. Se o valor não for uma lista, mas for iterável, retorne-o como uma lista. Se o valor não for iterável, retorne-o como uma lista de um único item.

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
