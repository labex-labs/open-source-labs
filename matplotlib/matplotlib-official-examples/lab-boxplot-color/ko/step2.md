# 임의의 테스트 데이터 생성

다음으로, `numpy` 라이브러리를 사용하여 임의의 테스트 데이터를 생성합니다. 각기 다른 표준 편차를 가진 3 개의 데이터 집합을 생성합니다.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
