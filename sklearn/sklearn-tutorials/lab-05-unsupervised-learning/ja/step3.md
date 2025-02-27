# ベクトル量子化

クラスタリングの応用例の1つがベクトル量子化です。ここでは、クラスタリングを使って少量のサンプルを選択して情報を圧縮します。たとえば、クラスタリングを使って画像をポスター化することができます。

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# Load a sample image
image = load_sample_image("china.jpg")
# Convert to grayscale
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Compress the image using cluster centers
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# Display original and compressed images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('Compressed Image')

plt.show()
```
