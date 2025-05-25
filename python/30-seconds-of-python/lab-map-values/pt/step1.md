# Mapear Valores do Dicionário

Escreva uma função `map_values(obj, fn)` que recebe um dicionário `obj` e uma função `fn` como argumentos e retorna um novo dicionário com as mesmas chaves do dicionário original e valores gerados pela execução da função fornecida para cada valor.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
