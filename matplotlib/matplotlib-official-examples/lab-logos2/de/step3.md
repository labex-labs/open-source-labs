# Erstellen der Icon-Achsen

In diesem Schritt erstellen wir eine Polarkoordinate, die den Matplotlib-Radarplot enthält.

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Erstellt eine Polarkoordinate, die den matplotlib-Radarplot enthält.

    Parameter
    ----------
    fig : matplotlib.figure.Figure
        Die Figur, in die gezeichnet werden soll.
    ax_position : (float, float, float, float)
        Die Position der erstellten Achse in Figurkoordinaten als
        (x, y, Breite, Höhe).
    lw_bars : float
        Die Linienstärke der Balken.
    lw_grid : float
        Die Linienstärke des Gitters.
    lw_border : float
        Die Linienstärke der Achsengrenze.
    rgrid : array-like
        Positionen des radialen Gitters.

    Rückgabe
    -------
    ax : matplotlib.axes.Axes
        Die erstellte Achse.
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
            color = *cm.jet(r / 10.)[:3], 0.6  # Farbe aus jet mit alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # der tatsächliche sichtbare Hintergrund - erstreckt sich etwas über die Achse hinaus
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
