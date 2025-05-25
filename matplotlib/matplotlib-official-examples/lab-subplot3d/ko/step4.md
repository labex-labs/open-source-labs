# 3D Wireframe Plot 생성

두 번째 서브플롯에 대한 3D wireframe plot 을 생성합니다. `mpl_toolkits.mplot3d.axes3d`에서 `get_test_data` 함수를 사용하여 plot 에 대한 데이터를 생성합니다.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
