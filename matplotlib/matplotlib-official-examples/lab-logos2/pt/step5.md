# Criando o Logotipo

Nesta etapa, criaremos a figura completa com o logotipo do Matplotlib.

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    Cria uma figura completa com o logotipo do Matplotlib.

    Parâmetros
    ----------
    height_px : int
        Altura da figura em pixels.
    lw_bars : float
        A espessura da linha da borda das barras.
    lw_grid : float
        A espessura da linha da grade.
    lw_border : float
        A espessura da linha da borda do ícone.
    rgrid : sequência de float
        As posições da grade radial.
    with_text : bool
        Se deve desenhar apenas o ícone ou incluir 'matplotlib' como texto.
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) if with_text else (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    if with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12, .17, 0.75) if with_text else (0.03, 0.03, .94, .94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```
