# Laden des Iris-Datensatzes und Plotten der Kovarianz der Merkmale

Wir beginnen, indem wir den Iris-Datensatz laden und die Kovarianz der Merkmale plotten, um zu sehen, wie sie korreliert sind.

```python
import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Laden Sie die Iris-Daten
data = load_iris()
X = StandardScaler().fit_transform(data["data"])
feature_names = data["feature_names"]

# Plotten der Kovarianz der Iris-Merkmale
ax = plt.axes()

im = ax.imshow(np.corrcoef(X.T), cmap="RdBu_r", vmin=-1, vmax=1)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(list(feature_names), rotation=90)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(list(feature_names))

plt.colorbar(im).ax.set_ylabel("$r$", rotation=0)
ax.set_title("Iris Merkmalskorrelationsmatrix")
plt.tight_layout()
```
