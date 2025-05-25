# Flat Shading (플랫 쉐이딩)

Matplotlib 의 `pcolormesh` 함수는 2D 그리드를 시각화할 수 있습니다. 가장 적은 가정을 가진 그리드 사양은 `shading='flat'`이며, 그리드의 각 차원에서 데이터보다 하나 더 큰 경우, 즉 `(M+1, N+1)` 형태를 갖는 경우입니다. 이 경우, `X`와 `Y`는 `Z`의 값으로 색칠된 사변형의 모서리를 지정합니다. 다음 코드 블록을 사용하여 그리드를 시각화할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
