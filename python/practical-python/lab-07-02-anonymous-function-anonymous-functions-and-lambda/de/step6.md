# Übung 7.6: Sortieren nach einem Feld mit lambda

Versuchen Sie, das Portfolio nach der Anzahl der Anteile mit einem `lambda`-Ausdruck zu sortieren:

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... überprüfen Sie das Ergebnis...
>>>
```

Versuchen Sie, das Portfolio nach dem Preis jeder Aktie zu sortieren

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... überprüfen Sie das Ergebnis...
>>>
```

Hinweis: `lambda` ist ein nützlicher Kurzweg, da es Ihnen ermöglicht, eine spezielle Verarbeitungsfunktion direkt im Aufruf von `sort()` zu definieren, im Gegensatz dazu, dass Sie zunächst eine separate Funktion definieren müssen.
