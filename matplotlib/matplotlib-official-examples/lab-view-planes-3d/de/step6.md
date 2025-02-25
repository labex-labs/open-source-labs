# Festlegen der Eigenschaften jeder primären 3D-Ansichtsebene

Wir legen die Eigenschaften jeder primären 3D-Ansichtsebene fest, einschließlich der Beschriftungen der x-, y- und z-Achsen, des Projektionstyps und der Blickwinkel.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
