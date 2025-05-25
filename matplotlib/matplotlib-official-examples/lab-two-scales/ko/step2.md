# 가짜 데이터 생성

다음으로, 플롯에 사용할 가짜 데이터를 생성합니다. `numpy.arange`를 사용하여 0.01 에서 10.0 까지 0.01 간격으로 값을 갖는 배열을 생성합니다. 그런 다음 `numpy.exp`와 `numpy.sin`을 사용하여 두 개의 데이터 세트를 생성합니다.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
