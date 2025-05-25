# 축 설정 함수 생성

원하는 눈금 레이블로 축을 설정하는 함수를 생성합니다.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
