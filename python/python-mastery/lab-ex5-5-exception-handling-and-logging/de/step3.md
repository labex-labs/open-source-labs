# Logging

Modifiziere den Code, sodass Warnmeldungen mit dem `logging`-Modul ausgegeben werden. Darüber hinaus gib optional Debug-Informationen an, die den Grund für das Versagen angeben. Beispielsweise:

```python
>>> import reader
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
WARNUNG:reader:Zeile 4: Schlechte Zeile: ['C', '', '53,08']
DEBUG:reader:Zeile 4: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 7: Schlechte Zeile: ['DIS', '50', 'N/A']
DEBUG:reader:Zeile 7: Grund: konnte Zeichenfolge nicht in float umwandeln: 'N/A'
WARNUNG:reader:Zeile 8: Schlechte Zeile: ['GE', '', '37,23']
DEBUG:reader:Zeile 8: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 13: Schlechte Zeile: ['INTC', '', '21,84']
DEBUG:reader:Zeile 13: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 17: Schlechte Zeile: ['MCD', '', '51,11']
DEBUG:reader:Zeile 17: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 19: Schlechte Zeile: ['MO', '', '70,09']
DEBUG:reader:Zeile 19: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 22: Schlechte Zeile: ['PFE', '', '26,40']
DEBUG:reader:Zeile 22: Grund: ungültiges Literal für int() mit Basis 10: ''
WARNUNG:reader:Zeile 26: Schlechte Zeile: ['VZ', '', '42,92']
DEBUG:reader:Zeile 26: Grund: ungültiges Literal für int() mit Basis 10: ''
>>>
```
