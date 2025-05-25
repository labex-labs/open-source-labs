# 데이터 생성

`sklearn.datasets` 라이브러리의 `make_blobs` 함수를 사용하여 샘플 데이터를 생성합니다. 이 함수는 클러스터링을 위해 등방성 가우시안 덩어리 (blob) 를 생성합니다.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
