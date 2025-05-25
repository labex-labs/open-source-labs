# 극좌표계에 산점도 생성

`plt.scatter()` 함수를 사용하여 극좌표계에 산점도를 생성합니다. `projection` 매개변수를 `'polar'`로 설정하고, 반지름, 각도, 색상 및 면적 값을 매개변수로 전달합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
