# Streudiagramm ohne autolimit_mode 'round_numbers'

In diesem Schritt werden wir ein Streudiagramm erstellen, ohne das autolimit_mode 'round_numbers' zu verwenden, und das Verhalten der automatischen Tick-Positionierung beobachten.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
