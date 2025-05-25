# Método format()

Existe um método `format()` que pode aplicar formatação a argumentos ou argumentos de palavra-chave (keyword arguments).

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

Francamente, `format()` é um pouco verboso. Eu prefiro f-strings.
