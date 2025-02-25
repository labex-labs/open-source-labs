# Definiere die Funktion zum Einrichten der Achsen

Als nächstes definieren Sie die `setup_axes()`-Funktion, die die polare Projektion des Graphen einrichtet. Diese Funktion verwendet ein `GridHelperCurveLinear`, um eine polare Projektion in einem rechteckigen Rahmen zu erstellen. Sie setzt auch die Grenzen des Graphen und gibt das `ax1`-Objekt zurück.

```python
def setup_axes(fig, rect):
    # Definiere die PolarAxes-Transformation und den Extremwertfinder
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # Definiere die Grid-Locatoren und -Formatter
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Definiere das GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # Erstelle das Achsenobjekt und setze seine Grenzen
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```
