# Übung 3.9: Ausnahmen fangen

Die von Ihnen geschriebene `parse_csv()`-Funktion wird verwendet, um den gesamten Inhalt einer Datei zu verarbeiten. In der Realität ist es jedoch möglich, dass Eingabedateien beschädigte, fehlende oder unsaubere Daten enthalten. Versuchen Sie dieses Experiment:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Ändern Sie die `parse_csv()`-Funktion, um alle `ValueError`-Ausnahmen, die während der Erstellung von Datensätzen generiert werden, zu fangen, und geben Sie eine Warnmeldung für Zeilen aus, die nicht konvertiert werden können.

Die Meldung sollte die Zeilennummer und Informationen über den Grund enthalten, warum der Konvertierungsversuch fehlschlug. Um Ihre Funktion zu testen, versuchen Sie, die obige Datei `missing.csv` zu lesen. Beispielsweise:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Zeile 4: Konvertierung von ['MSFT', '', '51.23'] nicht möglich
Zeile 4: Grund: invalid literal for int() with base 10: ''
Zeile 7: Konvertierung von ['IBM', '', '70.44'] nicht möglich
Zeile 7: Grund: invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
