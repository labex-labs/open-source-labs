# 데이터셋 생성

이 단계에서는 `sklearn.datasets` 모듈의 `make_gaussian_quantiles` 함수를 사용하여 두 개의 가우시안 쿼타일 클러스터로 구성된 비선형적으로 분리 가능한 분류 데이터셋을 생성합니다. 또한 두 클러스터를 연결하고 레이블을 할당합니다.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
