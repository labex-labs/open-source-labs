# Imagem e Barra de Cores com Posicionamento em Tempo de Desenho - Uma Abordagem Fácil

Nesta etapa, criaremos uma imagem e sua barra de cores com posicionamento em tempo de desenho de uma maneira fácil. Usaremos `make_axes_locatable` de `mpl_toolkits.axes_grid1` para criar um divisor para os eixos e a barra de cores.

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```
