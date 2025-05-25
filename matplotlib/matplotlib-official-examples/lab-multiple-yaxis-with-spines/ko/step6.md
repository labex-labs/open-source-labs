# 축의 제한 및 레이블 설정

`set` 메서드를 사용하여 각 y-axis 의 제한과 레이블을 설정합니다. 또한 `set_color` 메서드를 사용하여 레이블의 색상을 선의 색상과 일치하도록 설정합니다.

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```
