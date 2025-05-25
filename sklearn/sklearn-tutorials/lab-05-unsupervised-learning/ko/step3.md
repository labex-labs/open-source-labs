# 벡터 양자화

군집화의 한 응용 분야는 벡터 양자화입니다. 벡터 양자화에서는 군집화를 사용하여 정보를 압축하기 위해 소수의 예시 (exemplars) 를 선택합니다. 예를 들어, 군집화를 사용하여 이미지를 포스터화할 수 있습니다.

```python
import numpy as np
from sklearn import cluster, datasets
from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt

# 샘플 이미지 로드
image = load_sample_image("china.jpg")
# 그레이스케일로 변환
gray_image = image.mean(axis=2)

X = gray_image.reshape((-1, 1))

# K-평균 군집화 수행
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# 클러스터 중심을 사용하여 이미지 압축
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = gray_image.shape

# 원본 이미지와 압축된 이미지 표시
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('원본 이미지')

plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title('압축된 이미지')

plt.show()
```
