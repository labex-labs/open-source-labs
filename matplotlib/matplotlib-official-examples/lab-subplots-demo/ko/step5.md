# 극좌표 축 (Polar Axes)

`subplots()` 함수에 `projection='polar'` 매개변수를 전달하여 극좌표 `Axes` 그리드를 생성할 수 있습니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
