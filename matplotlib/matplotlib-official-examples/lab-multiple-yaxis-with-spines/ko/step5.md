# 플롯에 데이터 추가

`plot` 메서드를 사용하여 플롯에 데이터를 추가합니다. 각기 다른 y-axis 를 사용하는 세 개의 선을 플롯에 추가합니다.

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```
