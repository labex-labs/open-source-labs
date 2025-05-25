# 명시적 레벨을 사용한 채워진 등고선 생성

이제 명시적 레벨을 사용하여 채워진 등고선 플롯을 생성합니다. `contourf` 메서드를 사용하고 `levels` 매개변수를 값 목록으로 설정하여 등고선 레벨을 지정합니다. 또한 colormap 을 색상 목록으로 설정하고 `extend` 매개변수를 `'both'`로 설정하여 레벨 범위를 벗어나는 값을 표시합니다.

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```
