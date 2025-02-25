# Übung 1.23: Sortieren

Möchten Sie eine Liste sortieren? Verwenden Sie die `sort()`-Methode. Testen Sie es:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

Möchten Sie in umgekehrter Reihenfolge sortieren? Probieren Sie dies:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Hinweis: Beim Sortieren einer Liste werden deren Inhalte "in-place" geändert. Das heißt, die Elemente der Liste werden durcheinander gebracht, aber es wird keine neue Liste erstellt.
