# Creando los ejes del icono

En este paso, crearemos un eje polar que contendrá el gráfico de radar de Matplotlib.

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Crea un eje polar que contiene el gráfico de radar de matplotlib.

    Parámetros
    ----------
    fig : matplotlib.figure.Figure
        La figura en la que se dibujará.
    ax_position : (float, float, float, float)
        La posición del eje creado en coordenadas de figura como
        (x, y, ancho, alto).
    lw_bars : float
        El ancho de línea de las barras.
    lw_grid : float
        El ancho de línea de la cuadrícula.
    lw_border : float
        El ancho de línea del borde del eje.
    rgrid : array-like
        Posiciones de la cuadrícula radial.

    Devuelve
    -------
    ax : matplotlib.axes.Axes
        El eje creado.
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
            color = *cm.jet(r / 10.)[:3], 0.6  # color del jet con alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # el fondo visible real - se extiende un poco más allá del eje
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
