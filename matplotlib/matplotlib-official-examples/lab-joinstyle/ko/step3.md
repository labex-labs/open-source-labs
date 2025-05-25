# JoinStyle 설정

`Line2D` 객체의 `set_solid_joinstyle()` 메서드를 사용하여 선의 `JoinStyle`을 설정할 수 있습니다. 새로운 line 객체를 생성하고 join style 을 `JoinStyle.bevel`로 설정합니다.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
