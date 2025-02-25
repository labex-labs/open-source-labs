# Polare Projektion in einem rechteckigen Rahmen

Als nächstes erstellen wir eine polare Projektion in einem rechteckigen Rahmen mit `GridHelperCurveLinear`. Wir verwenden eine `Affine2D`-Transformation, um die Grad-Koordinaten in Radiant umzurechnen, und `PolarAxes.PolarTransform`, um die polare Projektion zu erstellen. Wir verwenden auch `angle_helper.ExtremeFinderCycle`, um die Extrema der polaren Projektion zu finden, und `angle_helper.LocatorDMS` und `angle_helper.FormatterDMS`, um die Strichelabels zu formatieren. Der folgende Code demonstriert diesen Prozess:

```python
def curvelinear_test2(fig):
    # Definiere die benutzerdefinierte Transformation
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # Definiere den Extremfinder, das Gitter-Locator und den Strichel-Formatter
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Erstelle GridHelperCurveLinear-Objekt
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # Mache die Strichelabels der rechten und oberen Achse sichtbar
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # Lasse die rechte Achse die Strichelabels für die erste Koordinate (Winkel) anzeigen
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # Lasse die untere Achse die Strichelabels für die zweite Koordinate (Radius) anzeigen
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # Setze das Seitenverhältnis und die Grenzen des Subplots
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # Füge Gitterlinien zum Subplot hinzu
    ax1.grid(True, zorder=0)

    # Erstelle eine Parasiten-Achse mit der angegebenen Transformation
    ax2 = ax1.get_aux_axes(tr)

    # Alles, was Sie in ax2 zeichnen, wird den Strichen und Gittern von ax1 entsprechen.
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test2(fig)
plt.show()
```
