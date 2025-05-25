# 간단한 화살표 생성

이제 `AnchoredDirectionArrows` 클래스를 사용하여 간단한 앵커된 방향 화살표를 생성합니다. 이 화살표는 플롯에서 X 및 Y 방향을 나타냅니다.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
