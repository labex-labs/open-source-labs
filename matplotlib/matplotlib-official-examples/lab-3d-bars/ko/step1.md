# 라이브러리 가져오기 및 Figure 설정

첫 번째 단계에서는 필요한 라이브러리를 가져오고 차트에 대한 figure 와 axes 를 설정합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
