# 데이터셋 생성

시각화를 위해 세 개의 데이터셋을 생성합니다. 첫 번째 데이터셋은 두 차원 모두에서 -3 과 3 사이의 균일 분포에서 랜덤하게 생성된 200 개의 샘플입니다. 두 번째 데이터셋은 `sklearn.datasets`의 `make_blobs` 함수를 사용하여 생성된 200 개의 샘플입니다. 세 번째 데이터셋 또한 `make_blobs` 함수를 사용하여 생성됩니다.

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
