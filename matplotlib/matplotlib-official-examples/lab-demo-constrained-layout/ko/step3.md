# Constrained Layout 없이 서브플롯 생성

*constrained layout*을 사용하지 않고 2x2 서브플롯이 있는 figure 를 생성합니다. 이로 인해 축 레이블이 겹치게 됩니다.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
