# 라이브러리 가져오기 및 데이터 생성

먼저 필요한 라이브러리를 가져오고 플로팅 (plotting) 을 위한 데이터를 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
