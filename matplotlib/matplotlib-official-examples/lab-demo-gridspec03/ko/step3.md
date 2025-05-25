# 서브플롯 주변 및 간격 제어

이 단계에서는 `GridSpec`을 사용하여 서브플롯 주변 및 간격을 제어합니다. 각각 3 개의 행과 3 개의 열을 가진 2 개의 gridspecs 를 사용하여 figure 를 생성합니다. 간격을 제어하기 위해 `left`, `right`, `bottom`, `top`, `wspace`, 및 `hspace` 매개변수를 지정합니다.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
