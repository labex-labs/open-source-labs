# Erstellen einer Liste

Verwenden Sie eckige Klammern, um einen Listenliteralen zu definieren:

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]
```

Manchmal werden Listen mit anderen Methoden erstellt. Beispielsweise kann eine Zeichenfolge mithilfe der `split()`-Methode in eine Liste unterteilt werden:

```python
>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
>>>
```
