# 데이터 생성

0 부터 15 까지 0.01 간격으로 값을 배열로 생성하고, basic_units 패키지의 radians 함수를 사용하여 라디안 (radians) 으로 변환합니다.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
