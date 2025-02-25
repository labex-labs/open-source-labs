# Triangulation-Objekt erstellen

Zunächst müssen wir ein Triangulation-Objekt erstellen. Wir werden die Klasse `Triangulation` aus `matplotlib.tri` verwenden. In diesem Beispiel werden wir ein Triangulation-Objekt mit zufälligen Daten erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generiere zufällige Daten
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
