# 라디안을 도 (Degrees) 로 변환

`rads_to_degrees`라는 Python 함수를 작성하세요. 이 함수는 라디안으로 표현된 각도를 나타내는 float 값인 `rad`라는 단일 인수를 받습니다. 이 함수는 각도를 도 단위의 float 값으로 반환해야 합니다. 다음 공식을 사용하여 라디안으로 표현된 각도를 도 단위로 변환할 수 있습니다.

```
degrees = radians * (180 / pi)
```

여기서 `pi`는 원의 둘레와 지름의 비율을 나타내는 상수 값으로, 대략 3.14159 와 같습니다.

함수는 `math` 모듈에서 `pi` 상수를 import 해야 합니다.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
