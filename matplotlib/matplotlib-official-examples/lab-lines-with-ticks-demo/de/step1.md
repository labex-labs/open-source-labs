# Bibliotheken importieren und Daten generieren

Wir werden zunächst die erforderlichen Bibliotheken importieren und einige Daten für die Darstellung generieren.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
