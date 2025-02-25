# Importieren von Matplotlib und Einrichten des Graphen

Zunächst müssen wir die Matplotlib-Bibliothek importieren und den Graphen einrichten. Wir werden einen leeren Graphen mit einer y-Achse und einer x-Achse erstellen. Wir werden auch die Achse so konfigurieren, dass nur die untere Spur sichtbar ist, die Tick-Positionen festlegen und die Tick-Länge definieren.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # nur die untere Spur anzeigen
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # Tick-Positionen definieren
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Tick Formatters")
```
