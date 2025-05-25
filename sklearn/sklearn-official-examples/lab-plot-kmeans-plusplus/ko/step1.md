# 샘플 데이터 생성

scikit-learn 라이브러리의 `make_blobs` 함수를 사용하여 샘플 데이터를 생성합니다. 이 함수는 클러스터링을 위해 등방성 가우시안 덩어리 (blobs) 를 생성합니다. 4 개의 중심을 가지는 4000 개의 샘플을 생성합니다.

```python
# 샘플 데이터 생성
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
