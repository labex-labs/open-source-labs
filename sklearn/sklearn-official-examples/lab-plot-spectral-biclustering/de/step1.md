# Beispiel-Daten generieren

Wir generieren die Beispiel-Daten mit der Funktion `make_checkerboard`. Jeder Pixel innerhalb von `shape=(300, 300)` repräsentiert mit seiner Farbe einen Wert aus einer gleichmäßigen Verteilung. Der Rauschen wird aus einer normalen Verteilung hinzugefügt, wobei der für `noise` gewählte Wert die Standardabweichung ist.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
