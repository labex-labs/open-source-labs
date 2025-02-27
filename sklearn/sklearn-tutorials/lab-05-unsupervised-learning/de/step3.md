# Vektorquantisierung

Eine Anwendung von Clustering ist die Vektorquantisierung, bei der wir Clustering verwenden, um eine kleine Anzahl von Exemplaren auszuwählen, um Informationen zu komprimieren. Beispielsweise können wir Clustering verwenden, um ein Bild zu posterisieren:

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# Lade ein Beispielbild
image = load_sample_image("china.jpg")
# Konvertiere es in Graustufen
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# Führe das K-Means-Clustering durch
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Komprimiere das Bild mit den Clusterzentren
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# Zeige das ursprüngliche und das komprimierte Bild an
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Originalbild')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('Komprimiertes Bild')

plt.show()
```
