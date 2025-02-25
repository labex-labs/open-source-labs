# Importieren der erforderlichen Module

Der erste Schritt besteht darin, die erforderlichen Module für unser Diagramm zu importieren. Wir werden `numpy` verwenden, um unsere x- und y-Daten zu generieren, `matplotlib.pyplot`, um das Diagramm zu erstellen, und `mpl_toolkits.axes_grid1`, um die zweite y-Achse zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```
