# 벽에 원 그리기

Matplotlib 의 `Circle` 및 `pathpatch_2d_to_3d` 함수를 사용하여 3D 플롯의 x=0 '벽'에 원을 그립니다.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
