# 이미지 사전 학습

MiniBatchKMeans 를 사용하여 이미지 사전을 학습합니다. 클러스터 수를 81 로 설정하고, 랜덤 상태를 설정하며, verbose 모드를 활성화합니다. 패치를 저장할 버퍼를 생성하고 데이터셋의 각 이미지를 반복합니다. 각 이미지에서 50 개의 패치를 추출하고 데이터를 재구성합니다. 그런 다음 데이터를 버퍼에 추가하고 인덱스를 증가시킵니다. 인덱스가 10 의 배수이면 버퍼를 연결하고 데이터에 partial_fit 을 실행합니다. 인덱스가 100 의 배수이면 지금까지 적합된 패치 수를 나타내는 메시지를 출력합니다.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# 온라인 학습 부분: 전체 데이터셋을 6 번 반복합니다.
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```
