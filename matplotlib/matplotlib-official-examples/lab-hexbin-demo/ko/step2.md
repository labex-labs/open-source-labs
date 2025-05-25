# 데이터 생성

`numpy.random.standard_normal()`과 `numpy.random.standard_normal()`을 사용하여 100,000 개의 데이터 포인트를 생성합니다. `standard_normal()`은 평균 0, 표준 편차 1 인 표준 정규 분포에서 임의의 숫자를 생성합니다.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
