# 데이터 시각화

이 단계에서는 생성된 데이터를 시각화합니다.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="예상 신호")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
