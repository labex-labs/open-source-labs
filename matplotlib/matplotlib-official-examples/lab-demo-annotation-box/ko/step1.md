# 점 플로팅

시작하기 위해 나중에 주석을 달 두 점을 플로팅해 보겠습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Define a 1st position to annotate (display it with a marker)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# Define a 2nd position to annotate (don't display with a marker this time)
xy2 = [0.3, 0.55]

# Fix the display limits to see everything
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
