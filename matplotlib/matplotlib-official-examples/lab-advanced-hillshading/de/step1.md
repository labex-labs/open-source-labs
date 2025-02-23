# Ein Farbverlauf für ein gefärbtes Diagramm anzeigen

In diesem Schritt lernen Sie, wie Sie einen korrekten numerischen Farbverlauf für ein gefärbtes Diagramm anzeigen.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LightSource, Normalize

def display_colorbar():
    """Display a correct numeric colorbar for a shaded plot."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    cmap = plt.cm.copper
    ls = LightSource(315, 45)
    rgb = ls.shade(z, cmap)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')

    # Use a proxy artist for the colorbar...
    im = ax.imshow(z, cmap=cmap)
    im.remove()
    fig.colorbar(im, ax=ax)

    ax.set_title('Using a colorbar with a shaded plot', size='x-large')
```
