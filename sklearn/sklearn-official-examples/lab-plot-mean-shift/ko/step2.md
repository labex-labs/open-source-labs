# 샘플 데이터 생성

다음으로 `sklearn.datasets` 모듈의 `make_blobs` 함수를 사용하여 샘플 데이터를 생성합니다. 10,000 개의 샘플과 중심점이 `[[1, 1], [-1, -1], [1, -1]]`이고 표준 편차가 0.6 인 세 개의 클러스터를 가진 데이터셋을 생성합니다.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
