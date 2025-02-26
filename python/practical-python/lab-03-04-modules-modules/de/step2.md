# Namensräume

Ein Modul ist eine Sammlung von benannten Werten und wird manchmal als _Namensraum_ bezeichnet. Die Namen sind alle globalen Variablen und Funktionen, die in der Quelldatei definiert sind. Nach dem Import wird der Modulname als Präfix verwendet. Daher der _Namensraum_.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

Der Modulname ist direkt an den Dateinamen gebunden (foo -> foo.py).
