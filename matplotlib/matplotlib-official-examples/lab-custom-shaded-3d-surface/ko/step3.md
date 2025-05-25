# 힐셰이딩 사용자 정의

이 단계에서는 내장 셰이딩을 재정의하고 "shade"에서 계산된 음영 처리된 표면의 RGB 색상을 전달하여 힐셰이딩을 사용자 정의합니다.

```python
# Set up plot
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
