# Das Diagramm anpassen

Matplotlib bietet eine Vielzahl von Anpassungsmöglichkeiten für Diagramme. Hier ist ein Beispielcode, der unser einfaches Liniendiagramm anpasst:

```python
import matplotlib.pyplot as plt

# Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Ein Diagramm erstellen
plt.plot(x, y, color='rot', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='gelb')

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Angepasstes Diagramm')

# Das Diagramm anzeigen
plt.show()
```

In diesem Code verwenden wir verschiedene Parameter der `plot()`-Methode, um das Diagramm anzupassen. Wir ändern die Farbe der Linie in rot, die Linienstärke auf 2, den Linienstil in gestrichelt (`--`), den Marker in einen Kreis (`o`), die Markergröße auf 8 und die Markerflächenfarbe in gelb.
