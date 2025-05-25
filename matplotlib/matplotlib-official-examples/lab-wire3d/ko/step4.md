# 플롯 사용자 정의

플롯을 시각적으로 더 매력적으로 만들기 위해 사용자 정의할 수 있습니다. 이 예제에서는 제목, 축 레이블을 추가하고 플롯의 색상을 변경합니다.

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
