# Laden des Iris-Datensatzes und Aufteilung der Daten

Wir werden den Iris-Datensatz laden, der ein in der Maschinellen Lernung weit verbreiteter Datensatz für Klassifizierungsaufgaben ist. Der Datensatz enthält 150 Stichproben von Iris-Blüten, wobei jede Stichprobe vier Merkmale hat: Kelchblattlänge, Kelchblattbreite, Blütenblattlänge und Blütenblattbreite. Wir werden den Datensatz in Eingangsmerkmale und Zielbezeichnungen aufteilen.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Lade den Iris-Datensatz
iris = datasets.load_iris()

# Teile den Datensatz in Eingangsmerkmale und Zielbezeichnungen auf
X = iris.data[:, :2] # Wir werden nur die ersten beiden Merkmale für die Visualisierung verwenden
y = iris.target
```
