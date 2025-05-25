# 범례에 그림자 효과 추가

`withSimplePatchShadow` 경로 효과를 사용하여 범례에 그림자 효과를 추가할 수 있습니다.

```python
# Create plot and add shadow effect to legend
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```
