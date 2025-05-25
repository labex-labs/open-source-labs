# 축 설정 함수 정의

코드를 단순화하기 위해, figure 객체와 위치를 입력으로 받아 사용자 정의 틱 레이블이 있는 axis 객체를 반환하는 함수를 정의할 수 있습니다.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
