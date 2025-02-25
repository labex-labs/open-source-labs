# Praktisches Beispiel - Vektorquantisierung

Betrachten wir ein praktisches Beispiel, in dem das Broadcasting nützlich ist. Betrachten Sie den in der Informationstheorie und der Klassifikation verwendeten Vektorquantisierungsalgorithmus (VQ). Die grundlegende Operation bei der VQ besteht darin, den am nächsten gelegenen Punkt in einer Punktmenge zu einem gegebenen Punkt zu finden. Dies kann mit Hilfe von Broadcasting erreicht werden. Hier ist ein Beispiel:

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

In diesem Beispiel repräsentiert `observation` das Gewicht und die Größe eines Athleten, der klassifiziert werden soll, und `codes` repräsentiert verschiedene Klassen von Athleten. Indem man `observation` von `codes` subtrahiert, wird das Broadcasting verwendet, um die Entfernung zwischen `observation` und jedem der Codes zu berechnen. Die `argmin`-Funktion wird dann verwendet, um den Index des am nächsten gelegenen Codes zu finden.
