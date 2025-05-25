# 데이터 시각화

Matplotlib 을 사용하여 생성된 데이터셋을 시각화할 것입니다. 다음 코드 블록에서는 각 데이터셋의 실제 클러스터를 보여주는 2x2 플롯을 만듭니다.

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

axs[0, 0].scatter(X[:, 0], X[:, 1], c=y)
axs[0, 0].set_title("가우시안 볼록 혼합")

axs[0, 1].scatter(X_aniso[:, 0], X_aniso[:, 1], c=y)
axs[0, 1].set_title("이방성 분포 볼록")

axs[1, 0].scatter(X_varied[:, 0], X_varied[:, 1], c=y_varied)
axs[1, 0].set_title("불균일 분산")

axs[1, 1].scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_filtered)
axs[1, 1].set_title("불균일 크기 볼록")

plt.suptitle("실제 클러스터").set_y(0.95)
plt.show()
```
