# Carregar os dados da imagem

Usaremos um exemplo de dados de imagem chamado `bivariate_normal.npy` de `cbook` para demonstrar o ImageGrid. Carregamos os dados da imagem usando a função `get_sample_data` de `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
