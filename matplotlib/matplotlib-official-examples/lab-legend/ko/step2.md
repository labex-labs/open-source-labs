# 데이터 생성

다음으로, 플롯에 사용할 가짜 데이터를 생성합니다. NumPy 의 `arange` 함수를 사용하여 `a`와 `b` 두 개의 배열을 생성합니다. 그런 다음 `exp` 함수를 사용하여 `a`와 `d`의 지수 값을 계산하여 `c`와 `d` 두 개의 배열을 더 생성합니다. `d`는 `c`의 역순입니다.

```python
# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]
```
