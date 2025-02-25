# Obtener imagen de demostración

En este paso, definiremos una función para obtener una imagen de demostración y su extensión. Utilizaremos la función `get_sample_data()` de `cbook` para obtener una imagen de muestra.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
