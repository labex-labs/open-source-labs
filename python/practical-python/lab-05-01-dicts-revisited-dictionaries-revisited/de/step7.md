# Ändern von Instanzen

Operationen, die ein Objekt ändern, aktualisieren das zugrunde liegende Wörterbuch.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name':'GOOG','shares': 100, 'price': 490.1 }
>>> s.shares = 50       # Festlegen
>>> s.date = '6/7/2007' # Festlegen
>>> s.__dict__
{ 'name': 'GOOG','shares': 50, 'price': 490.1, 'date': '6/7/2007' }
>>> del s.shares        # Löschen
>>> s.__dict__
{ 'name': 'GOOG', 'price': 490.1, 'date': '6/7/2007' }
>>>
```
