# Typumwandlungsregeln

Wenn es keine Kernschleifenimplementierung für die angegebenen Eingabetypen gibt, wird die Typumwandlung bei den Eingaben einer ufunc durchgeführt. Die Umwandlungsregeln bestimmen, wann ein Datentyp sicher in einen anderen Datentyp umgewandelt werden kann. Schauen wir uns ein Beispiel an.

```python
import numpy as np

# Überprüfen Sie, ob int sicher in float umgewandelt werden kann
result = np.can_cast(np.int, np.float)

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
True
```
