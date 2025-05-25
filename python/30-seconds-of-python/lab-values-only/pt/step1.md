# Valores de Dicionário

Você recebe um dicionário simples (flat dictionary) e precisa criar uma função que retorne uma lista simples (flat list) de todos os valores no dicionário. Sua tarefa é implementar a função `values_only(flat_dict)`, que recebe um dicionário simples como argumento e retorna uma lista de todos os valores no dicionário.

Para resolver este problema, você pode usar o método `dict.values()` para retornar os valores no dicionário fornecido. Em seguida, você pode converter o resultado em uma lista usando a função `list()`.

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
