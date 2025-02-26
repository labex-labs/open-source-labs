# Übung 7.5: Sortieren nach einem Feld

Versuchen Sie die folgenden Anweisungen, die das Portfolio-Daten alphabetisch nach dem Aktiennamen sortieren.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... überprüfen Sie das Ergebnis...
>>>
```

In diesem Teil extrahiert die `stock_name()`-Funktion den Namen einer Aktie aus einem einzelnen Eintrag in der `portfolio`-Liste. `sort()` verwendet das Ergebnis dieser Funktion, um den Vergleich durchzuführen.
