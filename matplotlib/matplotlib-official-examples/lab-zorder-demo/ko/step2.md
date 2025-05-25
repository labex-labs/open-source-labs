# Zorder 변경하기

아티스트의 그리기 순서를 변경하려면 아티스트를 생성할 때 `zorder` 매개변수를 사용하여 `zorder` 속성을 명시적으로 설정할 수 있습니다. 예를 들어, 산점도에서 점의 `zorder`를 선의 `zorder`보다 높은 값으로 설정하여 점을 선 위에 표시할 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.3, 1, 30)
theta = np.linspace(0, 4*np.pi, 30)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.2))

ax1.plot(x, y, 'C3', lw=3)
ax1.scatter(x, y, s=120)
ax1.set_title('Lines on top of dots')

ax2.plot(x, y, 'C3', lw=3)
ax2.scatter(x, y, s=120, zorder=2.5)  # move dots on top of line
ax2.set_title('Dots on top of lines')

plt.tight_layout()
plt.show()
```
