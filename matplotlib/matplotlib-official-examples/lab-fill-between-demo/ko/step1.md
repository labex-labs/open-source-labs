# 기본 사용법

`fill_between` 함수는 두 선 사이의 영역을 채우는 데 사용할 수 있습니다. _y1_ 및 _y2_ 매개변수는 스칼라 (scalar) 가 될 수 있으며, 주어진 y 값에서 수평 경계를 나타냅니다. *y1*만 제공된 경우, *y2*는 기본적으로 0 으로 설정됩니다.

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
```
