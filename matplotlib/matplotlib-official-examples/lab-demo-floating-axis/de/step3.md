# Definieren des Grid-Hilfsmittels

In diesem Schritt werden wir das Grid-Hilfsmittel definieren, das zur Erstellung der Polarkurve verwendet werden soll. Wir werden `GridHelperCurveLinear` verwenden, um das Grid-Hilfsmittel zu definieren.

```python
from mpl_toolkits.axisartist import GridHelperCurveLinear, HostAxes
import mpl_toolkits.axisartist.angle_helper as angle_helper

# Definieren des Grid-Hilfsmittels
extreme_finder = angle_helper.ExtremeFinderCycle(20,
                                                 20,
                                                 lon_cycle=360,
                                                 lat_cycle=None,
                                                 lon_minmax=None,
                                                 lat_minmax=(0, np.inf),
                                                 )
grid_locator1 = angle_helper.LocatorDMS(12)
tick_formatter1 = angle_helper.FormatterDMS()

grid_helper = GridHelperCurveLinear(tr,
                                    extreme_finder=extreme_finder,
                                    grid_locator1=grid_locator1,
                                    tick_formatter1=tick_formatter1
                                    )
```
