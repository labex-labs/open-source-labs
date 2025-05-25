# Obter Imagem de Demonstração

Nesta etapa, definiremos uma função para obter uma imagem de demonstração e sua extensão. Usaremos a função `get_sample_data()` de `cbook` para obter uma imagem de amostra.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
