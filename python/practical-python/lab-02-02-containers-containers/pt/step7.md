# Chaves Compostas (Composite keys)

Quase qualquer tipo de valor pode ser usado como uma chave de dicionário em Python. Uma chave de dicionário deve ser de um tipo que seja imutável. Por exemplo, tuplas:

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

Então, para acessar:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

_Nem uma lista, nem um conjunto (set), nem outro dicionário podem servir como uma chave de dicionário, porque listas e dicionários são mutáveis._
