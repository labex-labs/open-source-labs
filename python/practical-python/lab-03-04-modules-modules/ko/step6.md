# `import as` 구문

모듈을 임포트할 때 이름을 변경할 수 있습니다:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

이는 일반적인 import 와 동일하게 작동합니다. 단지 해당 파일 내에서 모듈의 이름을 변경할 뿐입니다.
