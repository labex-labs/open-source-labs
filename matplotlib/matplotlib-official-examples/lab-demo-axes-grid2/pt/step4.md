# Demonstração 1 - Barra de cores em cada eixo

Criaremos uma grade de 3 imagens com uma barra de cores em cada eixo usando o seguinte código:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- Criamos uma grade de 3 imagens usando `ImageGrid`.
- Definimos o `cbar_mode` como "each" para adicionar uma barra de cores em cada eixo.
- Definimos o parâmetro `share_all` como True para compartilhar os eixos x e y em todas as imagens.
- Definimos o parâmetro `cbar_location` como "top" para posicionar as barras de cores na parte superior.
- Definimos os `xticks` e `yticks` para a primeira imagem.
- Iteramos por cada imagem e adicionamos a imagem ao eixo usando `imshow`.
- Adicionamos uma barra de cores a cada eixo usando `ax.cax.colorbar`.
- Definimos as marcações da barra de cores para a segunda e terceira imagens.
- Adicionamos um título a cada imagem usando `add_inner_title`.
