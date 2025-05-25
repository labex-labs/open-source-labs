# 샘플 데이터 생성

`sklearn.datasets` 모듈의 `make_blobs` 함수를 사용하여 샘플 데이터셋을 생성합니다. `make_blobs` 함수는 n 차원 공간의 점들로 구성된 데이터셋을 생성하며, 각 점은 k 개의 클러스터 중 하나에 속합니다. 2 차원 공간에 300 개의 점으로 구성된 3 개의 클러스터를 가지며 표준 편차가 0.5 인 데이터셋을 생성합니다.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
