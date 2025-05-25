# K-평균 모델 적합

이미지 데이터의 작은 하위 샘플에 K-평균 모델을 적합하고 전체 이미지에 대한 색상 인덱스를 예측하는 데 사용합니다.

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# 데이터의 작은 하위 샘플에 K-평균 모델을 적합합니다.
print("데이터의 작은 하위 샘플에 모델 적합")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"done in {time() - t0:0.3f}s.")

# 모든 점에 대한 레이블 가져오기
print("전체 이미지에 대한 색상 인덱스 예측 (k-평균)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"done in {time() - t0:0.3f}s.")
```
