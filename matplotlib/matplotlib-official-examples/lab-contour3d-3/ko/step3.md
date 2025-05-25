# 3D 표면 플롯

이 단계에서는 테스트 데이터를 사용하여 3D 표면을 플롯하고 플롯의 모양을 사용자 정의합니다.

```python
# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Customize the appearance of the plot
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
