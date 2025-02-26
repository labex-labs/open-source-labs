# Übung 2.20: Sequenzreduzierungen

Berechnen Sie die Gesamtkosten des Portfolios mit einer einzigen Python-Anweisung.

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

Nachdem Sie das getan haben, zeigen Sie, wie Sie den aktuellen Wert des Portfolios mit einer einzigen Anweisung berechnen können.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Beide obigen Operationen sind ein Beispiel für eine Map-Reduction. Die Listenverständnis bildet eine Operation über die Liste ab.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

Die `sum()`-Funktion führt dann eine Reduzierung über das Ergebnis durch:

```python
>>> sum(_)
44671.15
>>>
```

Mit diesem Wissen sind Sie jetzt bereit, eine Big-Data-Startup-Gesellschaft zu gründen.
