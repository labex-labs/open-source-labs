# Mehrere Teilplots erstellen

In diesem Schritt werden wir lernen, wie mehrere Teilplots erstellt werden und wie die `fill_betweenx`-Funktion verwendet wird, um den Bereich zwischen zwei horizontalen Kurven in jedem Teilplot zu füllen.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, [ax1, ax2, ax3] = plt.subplots(1, 3, sharey=True, figsize=(12, 4))

ax1.fill_betweenx(y, 0, x1, color='green', alpha=0.5)
ax1.plot(x1, y, color='blue')
ax1.set_title('Fill between (x1, 0)')

ax2.fill_betweenx(y, x1, 1, color='red', alpha=0.5)
ax2.plot(x1, y, color='blue')
ax2.set_title('Fill between (x1, 1)')

ax3.fill_betweenx(y, x1, x2, color='orange', alpha=0.5)
ax3.plot(x1, y, color='blue')
ax3.plot(x2, y, color='red')
ax3.set_title('Fill between (x1, x2)')

plt.show()
```
