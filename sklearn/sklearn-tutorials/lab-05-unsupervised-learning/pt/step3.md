# Quantização Vetorial

Uma aplicação do agrupamento é a quantização vetorial, onde usamos o agrupamento para escolher um pequeno número de exemplares para comprimir informações. Por exemplo, podemos usar o agrupamento para posterizar uma imagem:

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# Carregar uma imagem de amostra
image = load_sample_image("china.jpg")
# Converter para escala de cinza
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# Executar o agrupamento K-means
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Comprimir a imagem usando os centros dos clusters
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# Exibir as imagens original e comprimida
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('Imagem Comprimida')

plt.show()
```
