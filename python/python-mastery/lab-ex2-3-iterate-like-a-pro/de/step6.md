# Generator-Ausdrücke und Reduktionsfunktionen

Generator-Ausdrücke eignen sich besonders gut, um Daten in Funktionen wie `sum()`, `min()`, `max()`, `any()` usw. zu übergeben. Versuchen Sie einige Beispiele mit den zuvor verwendeten Portfolio-Daten. Beachten Sie genau, dass in diesen Beispielen einige zusätzliche eckige Klammern (\[\]) fehlen, die bei der Verwendung von Listenkomprehensions auftauchten.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

Hier ist ein subtiler Gebrauch eines Generator-Ausdrucks bei der Erstellung von komma-getrennten Werten:

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... beobachten Sie, dass es fehlschlägt...
>>> ','.join(str(x) for x in s)    # Dies funktioniert
'GOOG,100,490.1'
>>>
```

Die Syntax in den obigen Beispielen bedarf einiger Übung, aber der entscheidende Punkt ist, dass keine der Operationen jemals eine vollständige Liste von Ergebnissen erstellt. Dies spart Ihnen viel Speicher. Sie müssen jedoch sicherstellen, dass Sie die Syntax nicht übertreiben.
