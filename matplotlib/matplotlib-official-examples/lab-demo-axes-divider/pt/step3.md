# Imagem Simples e Barra de Cores

Nesta etapa, criaremos uma imagem simples e sua barra de cores. Usaremos a função `imshow()` de `pyplot` para criar a imagem e a função `colorbar()` para criar a barra de cores.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
