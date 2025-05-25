# 특징 단변량 점수 시각화

각 특징의 단변량 점수를 플롯하여 어떤 특징이 중요한지 확인할 수 있습니다.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("특징 단변량 점수")
plt.xlabel("특징 번호")
plt.ylabel(r"단변량 점수 ($-Log(p_{value})$)")
plt.show()
```
