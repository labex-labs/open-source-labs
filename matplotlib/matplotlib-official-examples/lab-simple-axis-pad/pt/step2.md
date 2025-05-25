# Definir a Função de Configuração de Eixos

Em seguida, defina a função `setup_axes()`, que configura a projeção polar do gráfico. Esta função usa um `GridHelperCurveLinear` para criar uma projeção polar em uma caixa retangular. Ela também define os limites do gráfico e retorna o objeto `ax1`.

```python
def setup_axes(fig, rect):
    # Define the PolarAxes transform and the extreme finder
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # Define the grid locators and formatters
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Define the GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # Create the axis object and set its limits
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```
