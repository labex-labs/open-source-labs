# 플로팅 축 추가

플롯에 플로팅 축을 추가하는 두 개의 함수를 정의합니다. 첫 번째 함수 `add_floating_axis1()`은 `theta = 30` 레이블이 있는 플로팅 축을 플롯에 추가합니다. 두 번째 함수 `add_floating_axis2()`는 `r = 6` 레이블이 있는 플로팅 축을 플롯에 추가합니다.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
