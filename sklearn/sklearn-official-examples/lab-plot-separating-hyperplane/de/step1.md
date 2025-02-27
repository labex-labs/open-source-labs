# Erstellen eines zweiklassigen separablen Datensatzes

Um einen zweiklassigen separablen Datensatz zu erstellen, verwenden wir die Funktion `make_blobs()` aus scikit-learn. Diese Funktion generiert isotrope Gaussian Blobs für Clustering und Klassifikation. Wir werden 40 Proben mit zwei Zentren und einem Zufallszahlengenerator von 6 erstellen. Wir werden auch die Datenpunkte mit `matplotlib` visualisieren.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
