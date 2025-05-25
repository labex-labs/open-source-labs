# 필요한 라이브러리 가져오기 및 플롯 설정

먼저, 필요한 라이브러리를 가져오고 플롯을 설정해야 합니다. `matplotlib.pyplot`와 `numpy`를 사용합니다. 또한 데이터를 플롯할 figure 와 axis 객체를 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation of the bracket arrows relative to angleA and angleB")
```
