# `.Line2D.set_dashes()`를 사용하여 대시 시퀀스 수정

`.Line2D.set_dashes()`를 사용하여 대시 시퀀스를 수정할 수 있습니다. 이 예제에서는 `line1`의 대시 시퀀스를 수정하여 2pt 선, 2pt 간격, 10pt 선 및 2pt 간격의 대시 패턴을 만듭니다. 또한 `line1.set_dash_capstyle()`을 사용하여 캡 스타일을 'round'로 설정합니다.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
