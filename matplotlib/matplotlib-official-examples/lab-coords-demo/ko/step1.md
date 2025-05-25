# 사인파 플롯 생성

먼저, numpy 와 matplotlib 라이브러리를 사용하여 사인파 플롯을 생성해야 합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
