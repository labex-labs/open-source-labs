# Erstellen einer einfachen Farbskala

Um eine einfache Farbskala zu erstellen, können wir die Klasse `ListedColormap` aus dem Modul `matplotlib.colors` verwenden. Diese Klasse nimmt eine Liste von Farben entgegen und erstellt aus ihnen eine Farbskala.

```python
import matplotlib.colors as mcolors

# Definiere eine Liste von Farben
colors = ['red', 'green', 'blue']

# Erstelle ein ListedColormap-Objekt aus der Liste von Farben
cmap = mcolors.ListedColormap(colors)
```
