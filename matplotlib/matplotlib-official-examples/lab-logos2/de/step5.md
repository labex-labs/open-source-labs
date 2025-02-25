# Erstellen des Logos

In diesem Schritt erstellen wir die vollständige Figur mit dem Matplotlib-Logo.

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    Erstellt eine vollständige Figur mit dem Matplotlib-Logo.

    Parameter
    ----------
    height_px : int
        Höhe der Figur in Pixeln.
    lw_bars : float
        Die Linienstärke der Balkengrenzen.
    lw_grid : float
        Die Linienstärke des Gitters.
    lw_border : float
        Die Linienstärke der Icon-Grenze.
    rgrid : Folge von float
        Die Positionen des radialen Gitters.
    with_text : bool
        Ob nur das Icon gezeichnet werden soll oder 'matplotlib' als Text enthalten sein soll.
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) wenn with_text sonst (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    Wenn with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12,.17, 0.75) wenn with_text sonst (0.03, 0.03,.94,.94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```
