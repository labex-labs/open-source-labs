# Demonstração 2 - Barra de cores compartilhada

Criaremos uma grade de 3 imagens com uma barra de cores compartilhada usando o seguinte código:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- Criamos uma grade de 3 imagens usando `ImageGrid`.
- Definimos o `cbar_mode` como "single" para adicionar uma barra de cores compartilhada.
- Definimos o parâmetro `share_all` como True para compartilhar os eixos x e y em todas as imagens.
- Definimos o parâmetro `cbar_location` como "right" para posicionar a barra de cores à direita.
- Definimos os `xticks` e `yticks` para a primeira imagem.
- Iteramos por cada imagem e adicionamos a imagem ao eixo usando `imshow`.
- Definimos o parâmetro `clim` para garantir que todas as imagens usem a mesma escala de cores.
- Adicionamos uma barra de cores compartilhada ao eixo usando `ax.cax.colorbar`.
- Adicionamos um título a cada imagem usando `add_inner_title`.
