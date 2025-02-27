# Cuantización de vectores

Una aplicación del agrupamiento es la cuantización de vectores, donde usamos el agrupamiento para elegir un número pequeño de ejemplares para comprimir información. Por ejemplo, podemos usar el agrupamiento para posterizar una imagen:

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# Cargar una imagen de muestra
image = load_sample_image("china.jpg")
# Convertir a escala de grises
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# Realizar el agrupamiento K-means
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Comprimir la imagen usando los centros de los clusters
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# Mostrar las imágenes original y comprimida
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('Imagen Comprimida')

plt.show()
```
