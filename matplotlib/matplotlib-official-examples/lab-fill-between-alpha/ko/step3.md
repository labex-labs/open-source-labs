# `where`를 사용하여 특정 영역 강조하기

`where` 키워드 인수는 그래프의 특정 영역을 강조 표시하는 데 매우 유용합니다. `where`는 x, ymin 및 ymax 인수와 동일한 길이의 부울 마스크를 사용하며, 부울 마스크가 True 인 영역만 채웁니다. 아래 예제에서는 단일 무작위 보행자를 시뮬레이션하고 모집단 위치의 분석적 평균과 표준 편차를 계산합니다. 모집단 평균은 점선으로 표시되고, 평균에서 플러스/마이너스 1 시그마 편차는 채워진 영역으로 표시됩니다. `X > upper_bound` where 마스크를 사용하여 보행자가 1 시그마 경계 밖에 있는 영역을 찾고 해당 영역을 빨간색으로 음영 처리합니다.

```python
# Fixing random state for reproducibility
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# the steps and position
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# the 1 sigma upper and lower analytic population bounds
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='walker position')
ax.plot(t, mu*t, lw=1, label='population mean', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='1 sigma range')
ax.legend(loc='upper left')

# here we use the where argument to only fill the region where the
# walker is above the population 1 sigma boundary
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```
