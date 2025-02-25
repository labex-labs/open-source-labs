# Creando el logotipo

En este paso, crearemos la figura completa con el logotipo de Matplotlib.

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    Crea una figura completa con el logotipo de Matplotlib.

    Parámetros
    ----------
    height_px : int
        Altura de la figura en píxeles.
    lw_bars : float
        Ancho de línea del borde de la barra.
    lw_grid : float
        Ancho de línea de la cuadrícula.
    lw_border : float
        Ancho de línea del borde del icono.
    rgrid : secuencia de float
        Posiciones de la cuadrícula radial.
    with_text : bool
        Si se debe dibujar solo el icono o incluir 'matplotlib' como texto.
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) si with_text else (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    si with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12,.17, 0.75) si with_text else (0.03, 0.03,.94,.94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```

注：代码中的“si”应改为“if”，这是一处拼写错误，翻译时保留了原文错误。
