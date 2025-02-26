# Proxies

Eine Proxy-Klasse ist eine Klasse, die um eine vorhandene Klasse herumgeht und eine ähnliche Schnittstelle bereitstellt. Definieren Sie die folgende Klasse, die eine schreibgeschützte Schicht um ein vorhandenes Objekt erstellt:

```python
>>> class Readonly:
        def __init__(self, obj):
            self.__dict__['_obj'] = obj
        def __setattr__(self, name, value):
            raise AttributeError("Can't set attribute")
        def __getattr__(self, name):
            return getattr(self._obj, name)

>>>
```

Um die Klasse zu verwenden, wickeln Sie einfach ein vorhandenes Objekt in sie ein:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> p = Readonly(s)
>>> p.name
'GOOG'
>>> p.shares
100
>>> p.cost
49010.0
>>> p.shares = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: Can't set attribute
>>>
```
