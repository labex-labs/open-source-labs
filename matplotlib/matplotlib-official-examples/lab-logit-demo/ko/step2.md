# 로짓 스케일 (logit scale) 과 표준 표기법으로 플롯 생성

로짓 스케일과 표준 표기법을 사용하여 플롯을 생성합니다. 이는 `set_yscale("logit")`을 사용하여 y 축 스케일을 로짓으로 설정하고, `set_ylim()`을 사용하여 y 축 제한을 설정함으로써 수행할 수 있습니다. 또한 `plot()`을 사용하여 정규, 라플라시안, 코시 분포의 누적 분포 함수를 플롯하고, `legend()`를 사용하여 범례를 추가합니다.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```
