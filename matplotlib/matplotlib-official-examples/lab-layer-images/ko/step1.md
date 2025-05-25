# 필요한 라이브러리 임포트 및 함수 정의

필요한 라이브러리를 임포트하고 첫 번째 이미지를 생성하는 함수를 정의합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
