# 수평 영역 선택적 채우기

_where_ 매개변수를 사용하면 채울 x 범위를 지정할 수 있습니다. 이는 *x*와 동일한 크기의 부울 배열입니다. 연속된 _True_ 시퀀스의 x 범위만 채워집니다. 결과적으로, 인접한 *True*와 _False_ 값 사이의 범위는 절대 채워지지 않습니다. 따라서 데이터 포인트의 x 거리가 위 효과가 눈에 띄지 않을 정도로 충분히 세밀하지 않은 경우, `interpolate=True`를 설정하는 것이 좋습니다.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
