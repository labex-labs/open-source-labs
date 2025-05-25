# Power Law 정규화 생성

이 단계에서는 `PowerNorm()` 함수를 사용하여 Power Law 정규화를 생성해야 합니다.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
