# Encontrar a Chave de um Valor em um Dicionário

Escreva uma função `find_key(dict, val)` que encontre a primeira chave no dicionário fornecido que possui o valor dado.

Sua função deve:

- Receber um dicionário `dict` e um valor `val` como entrada.
- Usar `dictionary.items()` e `next()` para retornar a primeira chave que possui um valor igual a `val`.
- Retornar a chave como saída.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
