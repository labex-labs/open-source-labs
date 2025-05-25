# Chaves de Dicionário (Dictionary Keys)

Escreva uma função `keys_only(flat_dict)` que recebe um dicionário simples (flat dictionary) como entrada e retorna uma lista de todas as suas chaves.

Para resolver este problema, você pode seguir estes passos:

1. Use `dict.keys()` para retornar as chaves no dicionário fornecido.
2. Retorne uma `list()` do resultado anterior.

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
