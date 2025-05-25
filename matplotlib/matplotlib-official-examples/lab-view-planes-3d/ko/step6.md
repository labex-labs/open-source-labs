# 각 기본 3D 뷰 평면의 속성 설정

x, y, z 축의 레이블, 투영 유형 및 뷰 각도를 포함하여 각 기본 3D 뷰 평면의 속성을 설정합니다.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
