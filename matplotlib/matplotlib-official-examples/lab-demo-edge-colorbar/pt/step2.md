# Definir Dados da Imagem

Definimos uma função que retorna dados de imagem de exemplo e sua extensão.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
