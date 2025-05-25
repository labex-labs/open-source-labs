# 도에서 라디안으로 변환

인수를 도 (degrees) 로 받아 라디안 (radians) 으로 변환된 각도를 반환하는 함수 `degrees_to_rads(deg)`를 작성하십시오. 함수는 다음 공식을 사용하여 도를 라디안으로 변환해야 합니다.

```
radians = (degrees * pi) / 180.0
```

여기서 `pi`는 원의 둘레와 지름의 비율을 나타내는 상수 값 (약 3.14159) 입니다.

함수는 라디안으로 변환된 각도를 소수점 4 자리까지 반올림하여 반환해야 합니다.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
