# Preparar os dados de exemplo

Usaremos a função `get_sample_data` do cbook para obter dados de exemplo. Em seguida, prepararemos as imagens para serem exibidas na grade.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
