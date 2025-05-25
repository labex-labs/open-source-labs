# 모든 축에 데이터 플롯

`plot()` 메서드를 사용하여 모든 축에 데이터를 플롯합니다. 또한 `set()` 메서드를 사용하여 모든 축에 대한 레이블과 제한을 설정합니다.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")

host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
