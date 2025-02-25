# Proyección Polar en una Caja Rectangular

A continuación, crearemos una proyección polar en una caja rectangular utilizando `GridHelperCurveLinear`. Usaremos una transformación `Affine2D` para escalar las coordenadas de grados a radianes, y `PolarAxes.PolarTransform` para crear la proyección polar. También usaremos `angle_helper.ExtremeFinderCycle` para encontrar los extremos de la proyección polar, y `angle_helper.LocatorDMS` y `angle_helper.FormatterDMS` para formatear las etiquetas de las marcas. El siguiente código demuestra este proceso:

```python
def curvelinear_test2(fig):
    # Define the custom transform
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # Define the extreme finder, grid locator, and tick formatter
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Create GridHelperCurveLinear object
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # Make ticklabels of right and top axis visible
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # Let right axis show ticklabels for 1st coordinate (angle)
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # Let bottom axis show ticklabels for 2nd coordinate (radius)
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # Set the aspect ratio and limits of the subplot
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # Add grid lines to the subplot
    ax1.grid(True, zorder=0)

    # Create a parasite axes with the given transform
    ax2 = ax1.get_aux_axes(tr)

    # Anything you draw in ax2 will match the ticks and grids of ax1.
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test2(fig)
plt.show()
```
