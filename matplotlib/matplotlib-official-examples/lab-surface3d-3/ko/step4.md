# 표면 플롯 생성

이 단계에서는 우리가 만든 배열에서 가져온 면 색상으로 표면 플롯을 생성합니다. 또한 z 축을 사용자 정의합니다.

```python
# Create the surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# Show the plot
plt.show()
```
