# 축 방향 변경

이제 네 개의 서로 다른 플롯을 설정하기 위해 루프를 생성하고, 각 플롯에 네 개의 주요 방향으로 플로팅 축을 배치합니다. 루프 내에서 `add_floating_axis1()` 및 `add_floating_axis2()`를 사용하여 플로팅 축을 추가하고, `set_axis_direction()`을 사용하여 축 방향을 설정합니다.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
