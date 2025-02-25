# Benutzerdefinierte Legende erstellen

In diesem Schritt werden wir eine benutzerdefinierte Legende mit Matplotlib-Objekten erstellen. Zunächst importieren wir die `Line2D`-Klasse aus dem `matplotlib.lines`-Modul. Anschließend erstellen wir eine Liste von `Line2D`-Objekten mit benutzerdefinierten Attributen für Farbe, Breite und Bezeichnung. Schließlich zeichnen wir die Daten erneut mit der `plot`-Funktion und rufen `legend()` mit den benutzerdefinierten Linien und den entsprechenden Bezeichnungen auf.

```python
# Importiere die Line2D-Klasse
from matplotlib.lines import Line2D

# Erstelle benutzerdefinierte Linien
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Zeichne die Daten und generiere die benutzerdefinierte Legende
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
