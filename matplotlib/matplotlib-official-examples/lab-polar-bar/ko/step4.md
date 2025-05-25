# 극좌표 막대 차트 생성

`projection='polar'` 매개변수를 사용하여 극좌표 막대 차트를 생성합니다.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
