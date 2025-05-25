# 데이터셋 생성

다양한 클러스터링 알고리즘을 테스트하고 비교하기 위한 데이터셋이 생성됩니다. 다음과 같은 데이터셋이 생성됩니다.

- 잡음이 있는 원
- 잡음이 있는 초승달
- 블롭 (Blob)
- 구조 없음
- 이방성 분포 데이터
- 분산이 다른 블롭

```python
n_samples = 500

noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)
```
