# Ein einfaches Diagramm erstellen

Das einfachste Diagramm in Matplotlib ist ein Liniendiagramm. Sie können ein Liniendiagramm mit der `plot()`-Methode erstellen. Hier ist ein Beispielcode, der ein einfaches Liniendiagramm erstellt:

```python
import matplotlib.pyplot as plt

# Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Ein Diagramm erstellen
plt.plot(x, y)

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Einfaches Diagramm')

# Das Diagramm anzeigen
plt.show()
```

In diesem Code definieren wir zunächst unsere Datenpunkte als zwei Listen `x` und `y`. Wir erstellen dann ein Diagramm mit der `plot()`-Methode und übergeben unsere Datenpunkte. Wir fügen dann Beschriftungen für die X- und Y-Achsen und einen Titel für das Diagramm mit den Methoden `xlabel()`, `ylabel()` und `title()` hinzu. Schließlich zeigen wir das Diagramm mit der `show()`-Methode an.
