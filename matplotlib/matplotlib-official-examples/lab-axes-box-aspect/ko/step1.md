# 데이터와 무관한 정사각형 축

데이터 제한에 관계없이 정사각형 축을 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```
