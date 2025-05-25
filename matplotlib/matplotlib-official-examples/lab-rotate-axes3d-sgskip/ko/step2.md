# 3D 플롯 생성

다음으로, `plt.figure()` 및 `fig.add_subplot()` 함수를 사용하여 3D 플롯을 생성합니다. 또한 `ax.plot_wireframe()` 함수를 사용하여 데이터 세트를 와이어프레임으로 플롯합니다.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
