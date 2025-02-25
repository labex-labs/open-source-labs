# Warum Dictionaries?

Dictionaries sind nützlich, wenn es _viele_ verschiedene Werte gibt und diese Werte verändert oder manipuliert werden können. Dictionaries machen Ihren Code lesbarer.

```python
s['price']
# vs
s[2]
```

In den letzten Übungen haben Sie ein Programm geschrieben, das eine Datendatei `portfolio.csv` ausliest. Mit dem `csv`-Modul ist es einfach, die Datei Zeile für Zeile zu lesen.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name','shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Obwohl das Lesen der Datei einfach ist, möchten Sie oft mehr mit den Daten machen als nur lesen. Beispielsweise möchten Sie sie vielleicht speichern und einige Berechnungen damit durchführen. Leider gibt Ihnen eine einfache "Zeile" von Daten nicht genug, um damit zu arbeiten. Beispielsweise funktioniert auch eine einfache mathematische Berechnung nicht:

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Um mehr zu tun, möchten Sie die Rohdaten typischerweise auf eine bestimmte Weise interpretieren und in ein nützlicheres Objekt umwandeln, damit Sie später damit arbeiten können. Zwei einfache Optionen sind Tupel oder Dictionaries.
