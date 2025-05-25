# 자동 레벨을 사용한 채워진 등고선 생성

다음으로, 자동 레벨을 사용하여 채워진 등고선 플롯을 생성합니다. `cmap` 매개변수를 `plt.cm.bone`으로 설정하여 colormap 을 지정하는 `contourf` 메서드를 사용합니다. 또한 `contour` 메서드를 사용하여 등고선 라인을 추가하고, 채워진 등고선에 사용된 등고선 레벨의 하위 집합을 전달합니다.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
