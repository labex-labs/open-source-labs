# 矢量量化

聚类的一个应用是矢量量化，即我们使用聚类来选择少量的样本以压缩信息。例如，我们可以使用聚类来对图像进行色调分离：

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# 加载一张示例图像
image = load_sample_image("china.jpg")
# 转换为灰度图像
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# 执行 K 均值聚类
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# 使用聚类中心压缩图像
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# 显示原始图像和压缩后的图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('原始图像')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('压缩后的图像')

plt.show()
```
