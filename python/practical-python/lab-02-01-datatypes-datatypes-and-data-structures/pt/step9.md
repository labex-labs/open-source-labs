# Operações Comuns (Common operations)

Para obter valores de um dicionário, use os nomes das chaves.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

Para adicionar ou modificar valores, atribua usando os nomes das chaves.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

Para deletar um valor, use a instrução `del`.

```python
>>> del s['date']
>>>
```
