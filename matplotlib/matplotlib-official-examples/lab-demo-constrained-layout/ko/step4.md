# Constrained Layout 으로 서브플롯 생성

동일한 2x2 서브플롯을 생성하지만, 이번에는 *constrained layout*을 사용합니다. 이렇게 하면 축 객체와 레이블 간의 겹침을 방지하기 위해 서브플롯이 자동으로 조정됩니다.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
