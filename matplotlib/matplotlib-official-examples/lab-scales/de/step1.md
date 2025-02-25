# Bibliotheken importieren und Daten generieren

Zunächst müssen wir die erforderlichen Bibliotheken importieren und einige Daten generieren, um sie zu plotten. In diesem Beispiel werden wir eine Normalverteilung verwenden, um Daten für die y-Achse zu generieren.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
