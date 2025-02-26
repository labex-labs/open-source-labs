# Parte 4 : Diccionarios

En las últimas partes, simplemente ha trabajado con símbolos de acciones. Sin embargo, suponga que desea mapear símbolos de acciones a otros datos, como el precio. Utilice un diccionario:

```python
>>> prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
>>>
```

Un diccionario mapea claves a valores. Aquí está cómo acceder:

```python
>>> prices['IBM']
91.1
>>> prices['IBM'] = 123.45
>>> prices['HPQ'] = 26.15
>>> prices
{'GOOG': 490.1, 'AAPL': 312.23, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```

Para obtener una lista de claves, use esto:

```python
>>> list(prices)
['GOOG', 'AAPL', 'IBM', 'HPQ']
>>>
```

Para eliminar un valor, use `del`

```python
>>> del prices['AAPL']
>>> prices
{'GOOG': 490.1, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```
