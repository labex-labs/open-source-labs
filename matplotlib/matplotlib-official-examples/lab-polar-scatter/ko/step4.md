# 원점 오프셋이 있는 극좌표계에 산점도 생성

`PolarAxes` 객체의 `set_rorigin()` 및 `set_theta_zero_location()` 메서드를 설정하여 원점 오프셋이 있는 극좌표계에 산점도를 생성할 수 있습니다. 원점 반지름을 `-2.5`로 설정하고 세타 제로 위치를 `10`의 오프셋으로 `'W'`로 설정합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
