# 섹터로 제한된 극좌표계에 산점도 생성

`PolarAxes` 객체의 `set_thetamin()` 및 `set_thetamax()` 메서드를 설정하여 섹터로 제한된 극좌표계에 산점도를 생성할 수 있습니다. 세타 시작 및 종료 제한을 각각 `45`와 `135`로 설정합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
