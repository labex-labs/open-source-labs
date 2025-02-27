# Générer des données d'échantillonnage

Nous générons les données d'échantillonnage à l'aide de la fonction `make_checkerboard`. Chaque pixel dans `shape=(300, 300)` représente avec sa couleur une valeur provenant d'une distribution uniforme. Du bruit est ajouté à partir d'une distribution normale, où la valeur choisie pour `noise` est l'écart-type.

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
