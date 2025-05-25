# 학습 데이터 생성

이 단계에서는 클러스터링으로부터 학습 데이터를 생성합니다. scikit-learn 의 `make_blobs` 함수를 사용하여 표준 편차와 중심이 다른 3 개의 클러스터를 가진 5000 개의 샘플을 생성합니다.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
