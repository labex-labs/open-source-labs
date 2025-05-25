# Criar o gráfico

Em seguida, criaremos um gráfico usando alguns dados de exemplo. Usaremos uma distribuição normal bivariada como nossa fonte de dados.

```python
fig, ax = plt.subplots()

# make data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z
extent = (-3, 4, -4, 3)

ax.imshow(Z2, extent=extent, origin="lower")
```
