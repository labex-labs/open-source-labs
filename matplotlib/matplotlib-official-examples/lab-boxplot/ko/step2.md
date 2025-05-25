# 데이터 생성

예제에 사용할 임의의 데이터를 생성합니다. NumPy 함수 `random.lognormal()`을 사용하여 평균 1.5, 표준 편차 1.75 인 로그 정규 분포 (log-normal distribution) 데이터를 생성합니다. 4 개의 변수에 대해 37 개의 샘플을 생성하고, 이를 `data` 변수에 저장합니다. 또한 각 변수에 대한 레이블 목록을 생성합니다.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
