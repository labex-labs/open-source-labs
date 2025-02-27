# Quantification vectorielle

Une application du regroupement est la quantification vectorielle, où nous utilisons le regroupement pour choisir un nombre réduit d'exemplaires pour compresser l'information. Par exemple, nous pouvons utiliser le regroupement pour posteriser une image :

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# Chargez une image d'échantillonnage
image = load_sample_image("china.jpg")
# Convertissez en niveaux de gris
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# Effectuez un regroupement K-means
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Compressez l'image à l'aide des centres de cluster
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# Affichez les images d'origine et compressée
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Image d\'origine')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('Image compressée')

plt.show()
```
