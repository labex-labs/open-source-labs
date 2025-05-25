# Figure 및 Axes 생성

이 단계에서는 플롯을 위한 figure 와 axes 를 생성합니다. 또한 슬라이더를 위한 공간을 만들기 위해 axes 의 위치를 조정합니다.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
