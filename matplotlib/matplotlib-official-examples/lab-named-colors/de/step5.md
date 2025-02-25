# Ein Balkendiagramm erstellen

Wir können Matplotlib auch verwenden, um ein Balkendiagramm zu erstellen. In diesem Beispiel erstellen wir ein Balkendiagramm, das die Anzahl von verkauftem Äpfeln, Bananen und Orangen zeigt.

```python
import matplotlib.pyplot as plt

# Daten zum Plotten
äpfel = 10
bananen = 15
orangen = 5

# Erstellen des Balkendiagramms
plt.bar(["Äpfel", "Bananen", "Orangen"], [äpfel, bananen, oran gen])

# Festlegen des Titels
plt.title("Einfaches Balkendiagramm")

# Festlegen der x-Achsenbeschriftung
plt.xlabel("Früchte")

# Festlegen der y-Achsenbeschriftung
plt.ylabel("Menge")

# Anzeigen des Diagramms
plt.show()
```
