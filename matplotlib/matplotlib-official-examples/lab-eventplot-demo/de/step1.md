# Bibliotheken importieren und Zufallszahlengenerator initialisieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken und der Initialisierung eines Zufallszahlengenerators für die Reproduzierbarkeit.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
