# 플롯 사용자 정의

그리드 색상을 변경하고 범례를 추가하여 플롯을 사용자 정의할 수 있습니다. 이 예제에서는 겹침을 방지하기 위해 범례를 플롯 중심에서 약간 벗어나게 이동합니다.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))
```
