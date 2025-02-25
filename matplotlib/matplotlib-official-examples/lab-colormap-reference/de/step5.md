# Erstellen benutzerdefinierter Farbskalen

Matplotlib bietet auch die Möglichkeit, benutzerdefinierte Farbskalen zu erstellen. Dies kann nützlich sein, wenn die integrierten Farbskalen die gewünschte Darstellung der Daten nicht bieten.

```python
import matplotlib.colors as mcolors

# Definiere eine Liste von Farben und ihrer zugehörigen Werte
colors = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# Erstelle ein LinearSegmentedColormap-Objekt aus der Liste von Farben
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
