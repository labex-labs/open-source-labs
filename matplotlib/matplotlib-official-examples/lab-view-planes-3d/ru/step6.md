# Задаем свойства каждой основной трехмерной плоскости обзора

Мы задаем свойства каждой основной трехмерной плоскости обзора, включая метки для осей x, y и z, тип проекции и углы обзора.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
