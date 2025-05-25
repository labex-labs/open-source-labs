# 범례 및 축 색상 추가

`host.legend()` 메서드를 사용하여 호스트 축에 범례를 추가합니다. 또한 `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())`, 및 `par2.axis["right2"].label.set_color(p3.get_color())` 메서드를 사용하여 호스트 축의 왼쪽 y 축 레이블, 첫 번째 기생 축의 오른쪽 y 축 레이블, 그리고 두 번째 기생 축의 오른쪽 y 축 레이블의 색상을 해당 선과 일치하도록 설정합니다.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
