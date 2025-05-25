# 라이브러리 임포트 및 데이터 생성

먼저, 필요한 라이브러리를 임포트하고 플롯할 데이터를 생성해야 합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
origin = 'lower'
delta = 0.025
x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
