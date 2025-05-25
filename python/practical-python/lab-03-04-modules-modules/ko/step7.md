# `from` 모듈 임포트

이것은 모듈에서 선택된 심볼을 가져와 로컬에서 사용할 수 있도록 합니다.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

이를 통해 모듈 접두어를 입력하지 않고도 모듈의 일부를 사용할 수 있습니다. 자주 사용되는 이름에 유용합니다.
