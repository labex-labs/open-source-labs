# Bibliotheken importieren und Daten vorbereiten

Zunächst müssen wir die erforderlichen Bibliotheken importieren und einige Daten vorbereiten, um zu plottieren. In diesem Beispiel werden wir drei Sinuswellen mit zufälligem Rauschen darstellen.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up data
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
