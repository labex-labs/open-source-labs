# Establecer las propiedades de cada plano principal de vista tridimensional

Establecemos las propiedades de cada plano principal de vista tridimensional, incluyendo las etiquetas de los ejes x, y y z, el tipo de proyección y los ángulos de vista.

```python
for plane, angles in views:
    axd[plane].set_xlabel('x')
    axd[plane].set_ylabel('y')
    axd[plane].set_zlabel('z')
    axd[plane].set_proj_type('ortho')
    axd[plane].view_init(elev=angles[0], azim=angles[1], roll=angles[2])
    axd[plane].set_box_aspect(None, zoom=1.25)
```
