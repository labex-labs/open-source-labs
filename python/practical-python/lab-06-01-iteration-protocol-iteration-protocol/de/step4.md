# Übung 6.1: Iteration veranschaulicht

Erstellen Sie die folgende Liste:

```python
a = [1,9,4,25,16]
```

Iterieren Sie manuell über diese Liste. Rufen Sie `__iter__()` auf, um einen Iterator zu erhalten, und rufen Sie die `__next__()`-Methode auf, um aufeinanderfolgende Elemente zu erhalten.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

Die integrierte Funktion `next()` ist eine Abkürzung für das Aufrufen der `__next__()`-Methode eines Iterators. Versuchen Sie, sie auf einer Datei zu verwenden:

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # Hinweis: Dies gibt die Datei selbst zurück
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Rufen Sie immer wieder `next(f)` auf, bis Sie am Ende der Datei angelangt sind. Beobachten Sie, was passiert.
