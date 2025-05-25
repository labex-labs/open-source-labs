# 로그 스케일로 플롯 생성

이전 단계를 반복하지만, 이번에는 로그 스케일을 사용합니다. 로그 스케일은 정수 기반의 서브샘플링 (subsampling) 에 대해 마커 거리에서 시각적인 비대칭성을 유발하는 반면, 분수 기반의 서브샘플링은 균등한 분포를 생성합니다.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
