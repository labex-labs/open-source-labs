# 데이터 생성

이 단계에서는 `numpy.random.RandomState` 함수와 3 단계에서 정의된 매개변수를 사용하여 데이터를 생성합니다.

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
