# 결과 플롯

원본 혼합 신호, 원본 독립 소스, ICA 로 추정된 소스, PCA 로 추정된 소스를 플롯합니다.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "관측치 (혼합 신호)",
    "진짜 소스",
    "ICA 로 복원된 신호",
    "PCA 로 복원된 신호",
]
colors = ["red", "steelblue", "orange"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```
