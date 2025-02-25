# Ein Streudiagramm erstellen

Wir können Matplotlib auch verwenden, um ein Streudiagramm zu erstellen. In diesem Beispiel erstellen wir ein Streudiagramm, das die Beziehung zwischen den x- und y-Werten zeigt.

```python
import matplotlib.pyplot as plt

# x-Achsenwerte
x = [1, 2, 3, 4, 5]

# y-Achsenwerte
y = [2, 4, 6, 8, 10]

# Plotten der Punkte
plt.scatter(x, y)

# Festlegen des Titels
plt.title("Einfaches Streudiagramm")

# Festlegen der x-Achsenbeschriftung
plt.xlabel("X-Achse")

# Festlegen der y-Achsenbeschriftung
plt.ylabel("Y-Achse")

# Anzeigen des Diagramms
plt.show()
```
