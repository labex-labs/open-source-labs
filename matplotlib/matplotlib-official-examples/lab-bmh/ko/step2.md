# 베타 분포를 플롯하는 함수 정의

이 단계에서는 베타 분포를 플롯하는 함수를 정의합니다.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
