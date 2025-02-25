# Ein einfaches Diagramm erstellen

Jetzt, nachdem wir Matplotlib importiert haben, können wir es verwenden, um ein einfaches Diagramm zu erstellen. In diesem Beispiel erstellen wir einen Linienplot, der die Beziehung zwischen den x- und y-Werten zeigt.

```python
import matplotlib.pyplot as plt

# x-Achsenwerte
x = [1, 2, 3, 4, 5]

# y-Achsenwerte
y = [2, 4, 6, 8, 10]

# Zeichnen der Linie
plt.plot(x, y)

# Festlegen des Titels
plt.title("Einfacher Linienplot")

# Festlegen der x-Achsenbeschriftung
plt.xlabel("X-Achse")

# Festlegen der y-Achsenbeschriftung
plt.ylabel("Y-Achse")

# Anzeigen des Diagramms
plt.show()
```
