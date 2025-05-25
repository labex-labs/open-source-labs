# Figure 및 서브플롯 생성

이 단계에서는 누적 분포를 위한 두 개의 서브플롯이 있는 figure 를 생성합니다. 또한 figure 크기를 9x4 로 설정합니다.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
