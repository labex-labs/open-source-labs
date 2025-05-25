# 데이터 생성

이 실습에서는 임의의 데이터 세트를 생성합니다. 데이터 세트는 `x`, `y`, `z` 세 개의 변수를 가집니다. `x`와 `y`는 평균 0, 표준 편차 0.5 인 정규 분포 난수로 정의합니다. `z` 또한 평균 0, 표준 편차 0.1 인 정규 분포 난수입니다.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
