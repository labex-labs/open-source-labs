# 부동 축 추가 함수 정의

플롯에 부동 축을 추가하는 `add_floating_axis` 함수를 정의합니다. 이 함수는 `ax1` 객체를 인수로 받아 `axis` 객체를 반환합니다.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
