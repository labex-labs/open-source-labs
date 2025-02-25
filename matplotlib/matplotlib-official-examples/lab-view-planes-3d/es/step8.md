# Personalizar las etiquetas de marcas de graduación y las etiquetas de eje para cada plano principal de vista tridimensional

Personalizamos las etiquetas de marcas de graduación y las etiquetas de eje para cada plano principal de vista tridimensional para eliminar cualquier etiqueta innecesaria.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
