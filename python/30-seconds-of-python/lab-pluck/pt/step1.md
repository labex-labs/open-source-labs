# Extrair valores de uma lista de dicionários

Escreva uma função `pluck(lst, key)` que recebe uma lista de dicionários `lst` e uma chave (key) `key` como argumentos e retorna uma lista de valores correspondentes à `key` especificada.

Você precisa:

- Usar uma list comprehension e `dict.get()` para obter o valor da `key` para cada dicionário em `lst`.
- A função deve retornar uma lista vazia se a lista de entrada estiver vazia ou se a chave especificada não estiver presente em nenhum dos dicionários.

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```
