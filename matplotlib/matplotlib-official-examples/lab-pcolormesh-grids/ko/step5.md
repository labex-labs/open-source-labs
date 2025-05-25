# Nearest Shading, Same Shape Grid (가장 가까운 쉐이딩, 동일 형태 그리드)

일반적으로, `X`, `Y`, 그리고 `Z`를 모두 동일한 형태로 만들 때, 데이터의 행과 열을 삭제하는 것은 사용자가 의도하는 바가 아닙니다. 이 경우, Matplotlib 는 `shading='nearest'`를 허용하며, 색칠된 사변형을 그리드 포인트에 중심을 둡니다. `shading='nearest'`와 함께 올바르지 않은 형태의 그리드가 전달되면 오류가 발생합니다. 다음 코드 블록을 사용하여 그리드를 시각화할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
