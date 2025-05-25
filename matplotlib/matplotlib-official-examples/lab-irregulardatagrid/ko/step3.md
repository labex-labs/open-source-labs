# 그리드 (grid) 에서의 보간

불규칙하게 배치된 데이터 좌표의 등고선 플롯 (contour plot) 을 그리드 (grid) 에서의 보간을 통해 생성합니다. 먼저 `np.linspace`를 사용하여 x 및 y 에 대한 그리드 값을 생성합니다. 그런 다음 `tri.LinearTriInterpolator`를 사용하여 (xi, yi) 로 정의된 그리드에서 데이터 (x, y) 를 선형 보간합니다. 일반적인 `axes.Axes.contour`를 사용하여 보간된 데이터를 플롯합니다.

```python
ngridx = 100
ngridy = 200
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

fig, ax1 = plt.subplots()
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('Contour Plot of Irregularly Spaced Data Interpolated on a Grid')
fig.colorbar(cntr1, ax=ax1)
plt.show()
```
