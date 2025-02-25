# Importieren der erforderlichen Bibliotheken und Festlegen des Zufallszustands

Zunächst müssen wir die erforderlichen Bibliotheken importieren und den Zufallszustand für die Reproduzierbarkeit festlegen. Wir werden `numpy` verwenden, um einige zufällige Daten zu generieren, `matplotlib.pyplot` für die Erstellung von Visualisierungen und `cm` aus `matplotlib` für die Definition der Farbskalen.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
