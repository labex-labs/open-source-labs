# 선 아티스트 생성

이제 `matplotlib.lines`에서 `Line2D` 클래스를 사용하여 선 아티스트를 생성할 수 있습니다. x 및 y 좌표, 선 너비, 색상 및 축 객체를 인수로 지정할 수 있습니다.

```python
line = lines.Line2D(x, y, lw=2, color='black', axes=ax)
```
