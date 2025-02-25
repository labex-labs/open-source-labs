# Verwenden von Kurzschlussfunktionen

Das Modul `numpy.lib.npyio` bietet Kurzschlussfunktionen, die von `numpy.genfromtxt` abgeleitet sind. Diese Funktionen haben unterschiedliche Standardwerte und geben entweder ein standardmäßiges NumPy-Array oder ein maskiertes Array zurück.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
