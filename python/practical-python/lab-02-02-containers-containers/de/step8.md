# Mengen

Mengen sind Sammlungen ungeordneter, eindeutiger Elemente.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative Syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Mengen sind nützlich für die Prüfung auf Mitgliedschaft.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Mengen sind auch nützlich für die Entfernung von Duplikaten.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Zusätzliche Mengenoperationen:

```python
unique.add('CAT')        # Fügt ein Element hinzu
unique.remove('YHOO')    # Entfernt ein Element

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Mengenunion { 'a', 'b', 'c', 'd' }
s1 & s2                 # Mengenkreuzung { 'c' }
s1 - s2                 # Mengendifferenz { 'a', 'b' }
```

In diesen Übungen beginnen Sie mit der Erstellung eines der wichtigsten Programme, das für den Rest dieses Kurses verwendet wird. Arbeiten Sie in der Datei `report.py`.
