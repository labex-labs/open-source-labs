# Criando os Eixos do Ícone

Nesta etapa, criaremos um eixo polar contendo o gráfico de radar do Matplotlib.

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Cria um eixo polar contendo o gráfico de radar do matplotlib.

    Parâmetros
    ----------
    fig : matplotlib.figure.Figure
        A figura para desenhar.
    ax_position : (float, float, float, float)
        A posição dos eixos criados nas coordenadas da figura como
        (x, y, largura, altura).
    lw_bars : float
        A espessura das linhas das barras.
    lw_grid : float
        A espessura das linhas da grade.
    lw_border : float
        A espessura da linha da borda dos eixos.
    rgrid : array-like
        Posições da grade radial.

    Retorna
    -------
    ax : matplotlib.axes.Axes
        Os eixos criados.
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
            color = *cm.jet(r / 10.)[:3], 0.6  # color from jet with alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # the actual visible background - extends a bit beyond the axis
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
