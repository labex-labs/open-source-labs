# Broadcast-Beispiele

Schauen wir uns einige Beispiele an, um zu verstehen, wie das Broadcasting in verschiedenen Szenarien funktioniert.

- Beispiel 1:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

In diesem Fall wird `b` zu jeder Zeile von `a` addiert. Das Ergebnis ist ein 2D-Array mit der gleichen Form wie `a`, wobei jedes Element die Summe der entsprechenden Elemente in `a` und `b` ist.

- Beispiel 2:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

In diesem Fall scheitert das Broadcasting, weil die nachfolgenden Dimensionen von `a` und `b` nicht gleich sind. Es ist nicht möglich, die Werte in den Zeilen von `a` mit den Elementen von `b` für die elementweise Addition auszurichten.
