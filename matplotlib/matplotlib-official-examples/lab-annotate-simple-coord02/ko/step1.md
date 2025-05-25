# Matplotlib 임포트

Matplotlib 으로 플롯에 주석을 달기 전에 먼저 라이브러리를 임포트해야 합니다. 이 단계에서는 Matplotlib 을 임포트하고 주석 처리에 사용할 간단한 플롯을 생성합니다.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
