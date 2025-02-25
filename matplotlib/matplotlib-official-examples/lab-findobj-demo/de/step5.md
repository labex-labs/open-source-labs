# Erstellen verschiedener Diagrammtypen

Matplotlib unterstützt eine Vielzahl von Diagrammtypen, darunter Liniendiagramme, Streudiagramme, Balkendiagramme und mehr. Hier ist ein Beispielcode, der ein Streudiagramm erstellt:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generiere einige zufällige Daten
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Erstelle ein Streudiagramm
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Füge Achsenbeschriftungen und Titel hinzu
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Streudiagramm')

# Zeige das Diagramm an
plt.show()
```

In diesem Code verwenden wir die `scatter()`-Methode, um ein Streudiagramm zu erstellen. Wir generieren einige zufällige Daten mit der NumPy-Bibliothek und übergeben sie an die `scatter()`-Methode. Wir verwenden auch den `c`-Parameter, um die Farben der Datenpunkte anzugeben, den `s`-Parameter, um die Größen der Datenpunkte anzugeben, und den `alpha`-Parameter, um die Transparenz der Datenpunkte anzugeben.
