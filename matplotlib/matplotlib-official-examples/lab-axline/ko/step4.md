# 대각선 그리기

`transform` 매개변수를 사용하여 `axline`으로 고정된 기울기를 가진 대각선을 그릴 수 있습니다. 기울기가 `0.5`로 고정된 대각선 격자선을 그려보겠습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Draw diagonal lines
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
