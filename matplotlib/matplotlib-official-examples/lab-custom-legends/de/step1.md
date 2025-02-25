# Linien zeichnen

In diesem Schritt werden wir eine Reihe von Linien mit der Matplotlib-Bibliothek zeichnen. Zunächst erstellen wir einige zufällige Daten mit NumPy. Anschließend setzen wir den Farbzyklus mit der `cycler`-Funktion, um die Farbpalette anzugeben. Schließlich zeichnen wir die Daten mit der `plot`-Funktion und rufen `legend()` auf, um die Legende zu generieren.

```python
import matplotlib.pyplot as plt
import numpy as np

# Setze den Zufallszustand für Wiederholbarkeit
np.random.seed(19680801)

# Erstelle zufällige Daten
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Setze den Farbzyklus
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Zeichne die Daten und generiere die Legende
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
