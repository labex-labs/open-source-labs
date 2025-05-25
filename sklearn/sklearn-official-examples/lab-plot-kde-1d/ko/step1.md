# 히스토그램 및 커널 플롯

먼저 히스토그램과 커널을 플롯하여 두 가지 간의 차이점을 보여줍니다. 가우시안 커널 밀도 추정을 사용하여 두 가지 간의 차이점을 보여주고, scikit-learn 에서 사용 가능한 다른 커널들도 비교합니다.

```python
# 필요한 라이브러리 가져오기
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# 데이터 생성
np.random.seed(1)
N = 20
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
bins = np.linspace(-5, 10, 10)

# 그림 및 축 생성
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)

# 히스토그램 1 플롯
ax[0, 0].hist(X[:, 0], bins=bins, fc="#AAAAFF", density=True)
ax[0, 0].text(-3.5, 0.31, "히스토그램")

# 히스토그램 2 플롯
ax[0, 1].hist(X[:, 0], bins=bins + 0.75, fc="#AAAAFF", density=True)
ax[0, 1].text(-3.5, 0.31, "이동된 구간의 히스토그램")

# 톱햇 KDE 플롯
kde = KernelDensity(kernel="tophat", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 0].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 0].text(-3.5, 0.31, "톱햇 커널 밀도")

# 가우시안 KDE 플롯
kde = KernelDensity(kernel="gaussian", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 1].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 1].text(-3.5, 0.31, "가우시안 커널 밀도")

# 데이터 포인트 플롯
for axi in ax.ravel():
    axi.plot(X[:, 0], np.full(X.shape[0], -0.01), "+k")
    axi.set_xlim(-4, 9)
    axi.set_ylim(-0.02, 0.34)

# 왼쪽 열의 y 축 레이블 설정
for axi in ax[:, 0]:
    axi.set_ylabel("정규화된 밀도")

# 아래 행의 x 축 레이블 설정
for axi in ax[1, :]:
    axi.set_xlabel("x")

# 플롯 표시
plt.show()
```
