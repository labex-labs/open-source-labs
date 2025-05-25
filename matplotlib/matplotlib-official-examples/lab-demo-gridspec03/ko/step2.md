# `GridSpec`으로 서브플롯 생성

이 단계에서는 `GridSpec`을 사용하여 서브플롯을 생성합니다. 2 개의 행과 2 개의 열이 있는 figure 를 생성합니다. 또한 서브플롯의 상대적인 크기를 제어하기 위해 `width_ratios` 및 `height_ratios`를 지정합니다.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
