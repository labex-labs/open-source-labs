# Flat Shading, Same Shape Grid (플랫 쉐이딩, 동일 형태 그리드)

그리드가 각 차원에서 데이터와 동일한 형태를 갖는 경우, `shading='flat'`을 사용할 수 없습니다. 역사적으로 Matplotlib 는 이 경우 Matlab 의 동작과 일치시키기 위해 `Z`의 마지막 행과 열을 조용히 삭제했습니다. 이 동작이 여전히 필요한 경우, 마지막 행과 열을 수동으로 삭제하십시오. 다음 코드 블록을 사용하여 그리드를 시각화할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
