# Bibliotheken importieren und eine Figur erstellen

Der erste Schritt besteht darin, die erforderlichen Bibliotheken zu importieren und eine Figur zu erstellen. Wir verwenden das `matplotlib.pyplot`-Modul, um eine Figur zu erstellen, und das `mpl_toolkits.axes_grid1`-Modul, um Platz für die y-Beschriftung zu schaffen.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
