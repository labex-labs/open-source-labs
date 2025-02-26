# Ausnahmen fangen

Anstatt bei fehlerhaften Daten abzustürzen, modifiziere den Code, um stattdessen eine Warnmeldung auszugeben. Das endgültige Ergebnis sollte eine Liste der Zeilen sein, die erfolgreich konvertiert wurden. Beispielsweise:

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Zeile 4: Schlechte Zeile: ['C', '', '53,08']
Zeile 7: Schlechte Zeile: ['DIS', '50', 'N/A']
Zeile 8: Schlechte Zeile: ['GE', '', '37,23']
Zeile 13: Schlechte Zeile: ['INTC', '', '21,84']
Zeile 17: Schlechte Zeile: ['MCD', '', '51,11']
Zeile 19: Schlechte Zeile: ['MO', '', '70,09']
Zeile 22: Schlechte Zeile: ['PFE', '', '26,40']
Zeile 26: Schlechte Zeile: ['VZ', '', '42,92']
>>> len(port)
20
>>>
```

Hinweis: Das Durchführen dieser Änderung kann etwas schwierig sein, da Sie zuvor die integrierte Funktion `map()` verwendet haben. Sie müssen möglicherweise diese Vorgehensweise aufgeben, da es keine einfache Möglichkeit gibt, Ausnahmen in `map()` zu fangen und zu behandeln.
