# Criar uma Figura e ImageGrid

Em seguida, criamos uma figura e um ImageGrid com o parâmetro `nrows_ncols` para definir o número de linhas e colunas da grade.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
