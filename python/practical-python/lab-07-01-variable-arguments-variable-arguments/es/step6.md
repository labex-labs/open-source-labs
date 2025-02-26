# Ejercicio 7.2: Pasar tuplas y diccionarios como argumentos

Supongamos que lees algunos datos de un archivo y obtienes una tupla como esta:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Ahora, supongamos que quieres crear un objeto `Stock` a partir de estos datos. Si intentas pasar `data` directamente, no funciona:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

Esto se soluciona fácilmente usando `*data` en su lugar. Prueba esto:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Si tienes un diccionario, puedes usar `**` en su lugar. Por ejemplo:

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
