# 히스토그램 생성

이제 데이터를 얻었으므로 3D 히스토그램을 생성할 수 있습니다. NumPy 의 `histogram2d()` 함수를 사용하여 데이터의 2D 히스토그램을 생성한 다음, Matplotlib 의 `bar3d()` 함수를 사용하여 히스토그램의 3D 막대 그래프를 생성합니다.

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
