# Tripcolor 플롯 생성

이제 `tripcolor()` 함수를 사용하여 tripcolor 플롯을 생성합니다. 서로 다른 음영 처리 (shading) 방법을 사용하여 두 개의 플롯을 생성합니다.

```python
# Flat shading plot
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

# Gouraud shading plot
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('tripcolor of Delaunay triangulation, gouraud shading')
```
