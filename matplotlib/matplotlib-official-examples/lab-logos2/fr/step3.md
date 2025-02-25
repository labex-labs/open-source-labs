# Création des axes de l'icône

Dans cette étape, nous allons créer un axe polaire contenant le graphique radar de Matplotlib.

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Crée un axe polaire contenant le graphique radar de matplotlib.

    Paramètres
    ----------
    fig : matplotlib.figure.Figure
        La figure dans laquelle tracer.
    ax_position : (float, float, float, float)
        La position de l'Axe créé dans les coordonnées de la figure sous la forme
        (x, y, largeur, hauteur).
    lw_bars : float
        La largeur de ligne des barres.
    lw_grid : float
        La largeur de ligne de la grille.
    lw_border : float
        La largeur de ligne de la bordure de l'Axe.
    rgrid : array-like
        Positions de la grille radiale.

    Retours
    -------
    ax : matplotlib.axes.Axes
        L'Axe créé.
    """
    with plt.rc_context({'axes.edgecolor': MPL_BLUE,
                         'axes.linewidth': lw_border}):
        ax = fig.add_axes(ax_position, projection='polar')
        ax.set_axisbelow(True)

        N = 7
        arc = 2. * np.pi
        theta = np.arange(0.0, arc, arc / N)
        radii = np.array([2, 6, 8, 7, 4, 5, 8])
        width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])
        bars = ax.bar(theta, radii, width=width, bottom=0.0, align='edge',
                      edgecolor='0.3', lw=lw_bars)
        for r, bar in zip(radii, bars):
            color = *cm.jet(r / 10.)[:3], 0.6  # couleur issue de jet avec alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # le fond visible réel - s'étend un peu au-delà de l'axe
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
