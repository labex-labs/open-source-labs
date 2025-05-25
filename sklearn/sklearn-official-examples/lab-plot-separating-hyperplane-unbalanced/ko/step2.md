# 데이터 생성

`make_blobs` 함수를 사용하여 무작위 점의 두 개 클러스터를 생성합니다. 첫 번째 클러스터는 1000 개의 점으로, 두 번째 클러스터는 100 개의 점으로 생성합니다. 클러스터의 중심은 각각 `[0.0, 0.0]`과 `[2.0, 2.0]`입니다. `clusters_std` 매개변수는 클러스터의 표준 편차를 제어합니다.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
