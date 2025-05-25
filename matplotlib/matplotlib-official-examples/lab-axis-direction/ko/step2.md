# 축 설정 함수 생성

플롯의 축을 설정하기 위해 `setup_axes`라는 함수를 생성합니다. 이 함수는 `fig` 객체와 `pos` 객체, 두 개의 매개변수를 받습니다. `fig` 객체는 우리가 플로팅할 figure 객체이고, `pos` 객체는 figure 내의 서브플롯 위치입니다.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
