# 전체 축에 걸쳐 수평 영역 선택적 표시

동일한 선택 메커니즘을 사용하여 축의 전체 수직 높이를 채울 수 있습니다. y 제한과 독립적으로 유지하기 위해, x 값을 데이터 좌표로 해석하고 y 값을 축 좌표로 해석하는 변환 (transform) 을 추가합니다. 다음 예제는 y 데이터가 주어진 임계값 (threshold) 보다 높은 영역을 표시합니다.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
