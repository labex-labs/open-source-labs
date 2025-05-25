# 1 차원 밀도 예시 플롯

1 차원 공간에 100 개의 샘플을 사용하여 1 차원 밀도 예시를 플롯합니다. 톱햇, 가우시안, 에파네치니코프 세 가지 다른 커널 밀도 추정을 비교합니다.

```python
# 데이터 생성
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])

# 그림 및 축 생성
fig, ax = plt.subplots()

# 입력 분포 플롯
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="입력 분포")

# 색상 및 커널 설정
colors = ["navy", "cornflowerblue", "darkorange"]
kernels = ["gaussian", "tophat", "epanechnikov"]
lw = 2

# 커널 밀도 추정 플롯
for color, kernel in zip(colors, kernels):
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="커널 = '{0}'".format(kernel),
    )

ax.text(6, 0.38, "N={0}개의 점".format(N))

# 범례 및 데이터 포인트 플롯
ax.legend(loc="upper left")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")

# x 및 y 축 범위 설정
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)

# 플롯 표시
plt.show()
```
