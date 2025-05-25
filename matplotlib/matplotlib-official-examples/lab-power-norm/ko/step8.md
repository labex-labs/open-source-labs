# 멱법칙 정규화 생성

이 단계에서는 다양한 감마 값 (gamma values) 을 사용하여 멱법칙 정규화를 생성해야 합니다.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
