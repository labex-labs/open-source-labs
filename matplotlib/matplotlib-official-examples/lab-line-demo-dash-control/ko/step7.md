# 관련 메서드를 사용하여 대시의 다른 속성 설정

`~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()`, 및 `~.Line2D.set_gapcolor()`와 같은 관련 메서드를 사용하여 대시의 다른 속성도 설정할 수 있습니다. 이 예제에서는 `dashes` 및 `gapcolor` 매개변수를 사용하여 `line3`의 대시 시퀀스와 교대 색상을 설정합니다.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
