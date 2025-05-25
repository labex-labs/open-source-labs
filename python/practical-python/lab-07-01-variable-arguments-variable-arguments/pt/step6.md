# Exercício 7.2: Passando tuplas e dicionários como argumentos

Suponha que você leu alguns dados de um arquivo e obteve uma tupla como esta:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Agora, suponha que você queira criar um objeto `Stock` a partir desses dados. Se você tentar passar `data` diretamente, não funciona:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments: 'shares' and 'price'
>>>
```

Isso é facilmente corrigido usando `*data` em vez disso. Tente isto:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Se você tiver um dicionário, pode usar `**` em vez disso. Por exemplo:

```python
>>> data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
