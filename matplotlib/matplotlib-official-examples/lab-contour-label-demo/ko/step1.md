# 표면 정의

numpy 와 matplotlib 을 사용하여 표면을 정의하는 것으로 시작합니다. 이렇게 하면 작업할 데이터 세트가 제공됩니다.

```python
import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
