# Definieren unserer Fläche

Wir beginnen, indem wir unsere Fläche mit numpy und matplotlib definieren. Dies wird uns einen Datensatz liefern, mit dem wir arbeiten können.

```python
import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
