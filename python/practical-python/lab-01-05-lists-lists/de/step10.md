# Übung 1.22: Anhängen, Einfügen und Löschen von Elementen

Verwenden Sie die `append()`-Methode, um das Symbol `'RHT'` ans Ende von `symlist` hinzuzufügen.

```python
>>> symlist.append('RHT') # Anhängen von 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Verwenden Sie die `insert()`-Methode, um das Symbol `'AA'` als zweites Element in der Liste einzufügen.

```python
>>> symlist.insert(1, 'AA') # Einfügen von 'AA' als zweites Element in der Liste
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Verwenden Sie die `remove()`-Methode, um `'MSFT'` aus der Liste zu entfernen.

```python
>>> symlist.remove('MSFT') # Entfernen von 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Fügen Sie am Ende der Liste einen doppelten Eintrag für `'YHOO'` hinzu.

_Hinweis: Es ist völlig in Ordnung, wenn eine Liste doppelte Werte enthält._

```python
>>> symlist.append('YHOO') # Anhängen von 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Verwenden Sie die `index()`-Methode, um die erste Position von `'YHOO'` in der Liste zu finden.

```python
>>> symlist.index('YHOO') # Finden des ersten Index von 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Zählen Sie, wie oft `'YHOO'` in der Liste vorkommt:

```python
>>> symlist.count('YHOO')
2
>>>
```

Entfernen Sie das erste Vorkommen von `'YHOO'`.

```python
>>> symlist.remove('YHOO') # Entfernen des ersten Vorkommens von 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Damit Sie wissen, es gibt keine Methode, um alle Vorkommen eines Elements zu finden oder zu entfernen. Wir werden jedoch im Abschnitt 2 einen eleganten Weg dafür sehen.
