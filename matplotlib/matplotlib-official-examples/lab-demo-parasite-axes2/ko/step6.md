# 범례 및 색상 추가

`legend()` 및 `label.set_color()` 함수를 사용하여 플롯에 범례를 추가하고 각 축의 레이블 색상을 해당 데이터 세트의 색상과 일치시킵니다.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
