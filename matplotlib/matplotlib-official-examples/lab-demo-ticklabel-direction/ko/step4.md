# 바깥쪽을 가리키는 눈금 레이블

이 단계에서는 눈금 레이블이 바깥쪽을 가리키는 서브플롯을 생성합니다.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```
