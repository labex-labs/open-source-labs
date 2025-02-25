# Erstellen eines Graphen

Um einen Graphen zu erstellen, müssen wir zuerst die Daten definieren, die wir plotten möchten. In diesem Beispiel verwenden wir die `numpy`-Bibliothek, um einige Beispielsdaten zu generieren.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

Als nächstes erstellen wir eine neue Figur und Achse mit `plt.subplots()`. Wir setzen die x- und y-Bereiche des Graphen und plotten dann die Daten mit `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
