# Definir as propriedades de cada plano de visualização 3D primário

Definimos as propriedades de cada plano de visualização 3D primário, incluindo os rótulos para os eixos x, y e z, o tipo de projeção e os ângulos de visualização.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
