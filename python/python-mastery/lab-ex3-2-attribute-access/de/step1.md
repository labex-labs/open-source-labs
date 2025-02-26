# Die drei Operationen

Das gesamte Python-Objektsystem besteht nur aus drei Kernoperationen: das Abrufen, Setzen und Löschen von Attributen. Normalerweise werden diese über das Punktzeichen (.) wie folgt zugegriffen:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    #  Abrufen
'GOOG'
>>> s.shares = 50    # Setzen
>>> del s.shares     # Löschen
>>>
```

Die drei Operationen stehen auch als Funktionen zur Verfügung. Beispielsweise:

```python
>>> getattr(s, 'name')            # Identisch mit s.name
'GOOG'
>>> setattr(s,'shares', 50)      # Identisch mit s.shares = 50
>>> delattr(s,'shares')          # Identisch mit del s.shares
>>>
```

Die zusätzliche Funktion `hasattr()` kann verwendet werden, um zu prüfen, ob ein Objekt über ein bestimmtes Attribut verfügt:

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
