# 누적 분포 플롯

이 단계에서는 누적 분포를 플롯합니다. `.ecdf` 메서드를 사용하여 ECDF(경험적 누적 분포 함수) 와 보완 ECDF 를 플롯합니다. 또한 평균 200, 표준 편차 25 인 정규 분포를 사용하여 이론적 CDF(누적 분포 함수) 를 플롯합니다.

```python
# Cumulative distributions
axs[0].ecdf(data, label="CDF")
n, bins, patches = axs[0].hist(data, 25, density=True, histtype="step",
                               cumulative=True, label="Cumulative histogram")
x = np.linspace(data.min(), data.max())
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (x - mu))**2))
y = y.cumsum()
y /= y[-1]
axs[0].plot(x, y, "k--", linewidth=1.5, label="Theory")

# Complementary cumulative distributions
axs[1].ecdf(data, complementary=True, label="CCDF")
axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
            label="Reversed cumulative histogram")
axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")
```
