# 데이터 플롯

밀도, 온도 및 속도, 세 개의 데이터 세트를 동일한 플롯에 플롯합니다. `plot()` 함수를 사용하여 데이터를 플롯합니다.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
