# Plotten mit Rändern

Die `margins()`-Methode in Matplotlib kann verwendet werden, um Ränder im Plot festzulegen, anstatt die `set_xlim()`- und `set_ylim()`-Methoden zu verwenden. In diesem Schritt werden wir lernen, wie man mit der `margins()`-Methode in- und auszoomen kann, anstatt mit den `set_xlim()`- und `set_ylim()`-Methoden.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# Erstellen eines Teilplots mit Rändern
ax1 = plt.subplot(212)
ax1.margins(0.05) # Standardrand ist 0.05, Wert 0 bedeutet Anpassen
ax1.plot(t1, f(t1))

# Erstellen eines Teilplots mit vergrößertem Rand
ax2 = plt.subplot(221)
ax2.margins(2, 2) # Werte >0.0 vergrößern
ax2.plot(t1, f(t1))
ax2.set_title('Vergrößert')

# Erstellen eines Teilplots mit verkleinertem Rand
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # Werte in (-0.5, 0.0) verkleinern zum Zentrum hin
ax3.plot(t1, f(t1))
ax3.set_title('Verkleinert')

plt.show()
```
