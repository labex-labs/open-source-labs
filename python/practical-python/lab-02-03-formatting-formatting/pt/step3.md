# Formatação de Dicionários

Você pode usar o método `format_map()` para aplicar formatação de strings a um dicionário de valores:

```python
>>> s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

Ele usa os mesmos códigos que `f-strings`, mas pega os valores do dicionário fornecido.
