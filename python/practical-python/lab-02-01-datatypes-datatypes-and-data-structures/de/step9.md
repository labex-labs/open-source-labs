# Allgemeine Operationen

Um Werte aus einem Dictionary zu erhalten, verwenden Sie die Schlüsselnamen.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

Um Werte hinzuzufügen oder zu ändern, weisen Sie die Werte über die Schlüsselnamen zu.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

Um einen Wert zu löschen, verwenden Sie den `del`-Befehl.

```python
>>> del s['date']
>>>
```
