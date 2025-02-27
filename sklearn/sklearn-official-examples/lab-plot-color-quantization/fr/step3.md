# Ajuster le modèle K-Means

Nous allons ajuster le modèle K-Means sur un petit sous-échantillonnage des données d'image, et l'utiliser pour prédire les indices de couleur sur l'image complète.

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# Ajuster le modèle K-Means sur un petit sous-échantillonnage des données
print("Ajustement du modèle sur un petit sous-échantillonnage des données")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"terminé en {time() - t0:0.3f}s.")

# Obtenir les étiquettes pour tous les points
print("Prédiction des indices de couleur sur l'image complète (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"terminé en {time() - t0:0.3f}s.")
```
