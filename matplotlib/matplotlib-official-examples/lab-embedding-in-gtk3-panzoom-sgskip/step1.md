# Import Required Libraries

First, we need to import the required libraries. We will be using `gi` library to access GTK3 widgets, and Matplotlib's `FigureCanvas` and `NavigationToolbar` for embedding a plot with navigation toolbar.

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
```
