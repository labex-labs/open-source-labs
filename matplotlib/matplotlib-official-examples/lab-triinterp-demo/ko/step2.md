# 선형 방법 (Linear Method) 을 사용하여 데이터 보간

두 번째 단계는 선형 방법 (linear method) 을 사용하여 데이터를 보간하는 것입니다. 정규 간격의 사각 그리드 (quad grid) 를 생성한 다음 LinearTriInterpolator 메서드를 사용하여 데이터를 보간합니다. 마지막으로 보간된 데이터를 플롯 (plot) 합니다.

```python
# Interpolate to regularly-spaced quad grid.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpolate using linear method.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
