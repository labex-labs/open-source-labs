# Ein Kreisdiagramm erstellen

Wir können Matplotlib auch verwenden, um ein Kreisdiagramm zu erstellen. In diesem Beispiel erstellen wir ein Kreisdiagramm, das den Anteil der Menschen zeigt, die verschiedene Arten von Pizza bevorzugen.

```python
import matplotlib.pyplot as plt

# Daten zum Plotten
größen = [30, 40, 10, 20]
beschriftungen = ["Pepperoni", "Pilz", "Zwiebel", "Würstchen"]

# Erstellen des Kreisdiagramms
plt.pie(größen, labels=beschriftungen, autopct='%1.1f%%')

# Festlegen des Titels
plt.title("Einfaches Kreisdiagramm")

# Anzeigen des Diagramms
plt.show()
```
