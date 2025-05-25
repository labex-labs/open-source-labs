# 시각화

Matplotlib 를 사용하여 서로 다른 구성 요소를 시각화할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.scatter(component_1[:, 0], component_1[:, 1], s=0.8)
plt.scatter(component_2[:, 0], component_2[:, 1], s=0.8)
plt.title("가우시안 혼합 구성 요소")
plt.axis("equal")
plt.show()
```
