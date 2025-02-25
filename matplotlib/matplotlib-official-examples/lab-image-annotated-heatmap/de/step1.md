# Einfache kategorische Heatmap

Wir beginnen mit der Definition einiger Daten. Wir benötigen eine 2D-Liste oder -Array, das die zu farbkodierenden Daten definiert. Anschließend benötigen wir auch zwei Listen oder Arrays von Kategorien. Die Heatmap selbst ist ein `imshow`-Diagramm mit den Labels auf die Kategorien gesetzt. Wir werden die `text`-Funktion verwenden, um die Daten selbst zu beschriften, indem wir in jeder Zelle ein `Text` erstellen, das den Wert dieser Zelle zeigt.

```python
import matplotlib.pyplot as plt
import numpy as np

gemüsesorten = ["Gurke", "Tomate", "Salat", "Spargel", "Kartoffel", "Weizen", "Gerste"]
bauer = ["Bauer Joe", "Upland Bros.", "Smith Gardening", "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

ernte = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                  [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                  [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                  [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                  [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                  [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                  [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

fig, ax = plt.subplots()
im = ax.imshow(ernte)

# Zeige alle Striche und beschrifte sie mit den jeweiligen Listeinträgen
ax.set_xticks(np.arange(len(bauer)), labels=bauer)
ax.set_yticks(np.arange(len(gemüsesorten)), labels=gemüsesorten)

# Drehe die Strichmarkenbeschriftungen und setze ihre Ausrichtung
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Schleife über die Daten Dimensionen und erstelle Textanmerkungen
for i in range(len(gemüsesorten)):
    for j in range(len(bauer)):
        text = ax.text(j, i, ernte[i, j], ha="center", va="center", color="w")

ax.set_title("Ernte der örtlichen Bauern (in Tonnen/ Jahr)")
fig.tight_layout()
plt.show()
```
