# 여러 개의 시각화 객체를 하나의 그림에 결합

시각화 객체는 인수로 전달된 계산된 값을 저장합니다. 이를 통해 Matplotlib API 를 사용하여 시각화를 쉽게 결합할 수 있습니다. 다음 예제에서는 그림에 두 개의 시각화를 가로로 나란히 배치합니다.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
