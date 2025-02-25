# Création du logo

Dans cette étape, nous allons créer la figure complète avec le logo de Matplotlib.

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    Crée une figure complète avec le logo de Matplotlib.

    Paramètres
    ----------
    height_px : int
        Hauteur de la figure en pixels.
    lw_bars : float
        Largeur de ligne de la bordure des barres.
    lw_grid : float
        Largeur de ligne de la grille.
    lw_border : float
        Largeur de ligne de la bordure de l'icône.
    rgrid : séquence de float
        Positions de la grille radiale.
    with_text : bool
        Indique s'il faut seulement dessiner l'icône ou inclure'matplotlib' sous forme de texte.
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) si with_text sinon (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    if with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12,.17, 0.75) si with_text sinon (0.03, 0.03,.94,.94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```
