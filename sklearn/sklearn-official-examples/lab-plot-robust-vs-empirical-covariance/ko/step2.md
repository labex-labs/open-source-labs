# 데이터 생성

이 단계에서는 `n_samples`개의 샘플과 `n_features`개의 특징을 가진 무작위 데이터 집합을 생성합니다. 또한 데이터 집합에 일부 이상치를 추가합니다.

```python
n_samples = 80
n_features = 5

# 무작위 데이터 집합 생성
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# 데이터 집합에 이상치 추가
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
