# 선형 스케일 (linear scale) 로 플롯 생성

선형 스케일로 플롯을 생성합니다. 이는 `plot()`을 사용하여 정규, 라플라시안, 코시 분포의 누적 분포 함수를 플롯하고, `legend()`를 사용하여 범례를 추가함으로써 간단하게 수행할 수 있습니다.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```
