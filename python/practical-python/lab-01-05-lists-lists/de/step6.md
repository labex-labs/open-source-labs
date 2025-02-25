# Listen und Mathematik

_Vorsicht: Listen wurden nicht für mathematische Operationen entwickelt._

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

Insbesondere stellen Listen keine Vektoren/Matrizen wie in MATLAB, Octave, R usw. dar. Es gibt jedoch einige Pakete, die Ihnen dabei helfen (z.B. [numpy](https://numpy.org)).

In diesem Übungsaufgaben verwenden wir den Listen-Datentyp in Python. Im letzten Abschnitt haben Sie mit Zeichenketten gearbeitet, die Aktiensymbole enthielten.

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Teilen Sie es in eine Liste von Namen auf, indem Sie die `split()`-Operation von Zeichenketten verwenden:

```python
>>> symlist = symbols.split(',')
```
