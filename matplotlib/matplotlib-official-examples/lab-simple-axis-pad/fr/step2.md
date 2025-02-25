# Définir la fonction de configuration des axes

Ensuite, définissez la fonction `setup_axes()`, qui configure la projection polaire du graphique. Cette fonction utilise un `GridHelperCurveLinear` pour créer une projection polaire dans un cadre rectangulaire. Elle définit également les limites du graphique et renvoie l'objet `ax1`.

```python
def setup_axes(fig, rect):
    # Définir la transformation PolarAxes et le chercheur d'extrémités
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # Définir les localisateurs et les formatteurs de grille
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Définir le GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # Créer l'objet d'axe et définir ses limites
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```
