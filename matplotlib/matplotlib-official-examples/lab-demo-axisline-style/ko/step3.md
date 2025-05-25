# 축 스타일 구성

이제 각 축의 끝에 화살표를 추가하고 원점에서 X 축과 Y 축을 추가하여 축 스타일을 구성합니다.

```python
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
