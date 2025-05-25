# 라이브러리 임포트 및 이미지 정의

첫 번째 단계에서는 필요한 라이브러리를 임포트하고 예제에 사용될 이미지를 정의합니다. 이미지는 두 개의 가우시안 함수 (Gaussian function) 의 조합입니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

def get_image():
    delta = 0.25
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2)
    return Z
```
