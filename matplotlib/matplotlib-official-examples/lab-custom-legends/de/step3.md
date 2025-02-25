# Benutzerdefinierte Legende mit verschiedenen Matplotlib-Objekten erstellen

In diesem Schritt werden wir eine benutzerdefinierte Legende mit verschiedenen Matplotlib-Objekten erstellen, darunter `Line2D` und `Patch`. Zunächst importieren wir die `Patch`-Klasse aus dem `matplotlib.patches`-Modul. Anschließend erstellen wir eine Liste von `Line2D`- und `Patch`-Objekten mit benutzerdefinierten Attributen. Schließlich rufen wir `legend()` mit den benutzerdefinierten Objekten und den entsprechenden Bezeichnungen auf.

```python
# Importiere die Line2D- und Patch-Klassen
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Erstelle die Legendelemente
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Zeichne die Daten und generiere die benutzerdefinierte Legende
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
