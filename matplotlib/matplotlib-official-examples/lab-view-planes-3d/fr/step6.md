# Définissez les propriétés de chaque plan de vue principal 3D

Nous définissons les propriétés de chaque plan de vue principal 3D, y compris les étiquettes pour les axes x, y et z, le type de projection et les angles de vue.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
