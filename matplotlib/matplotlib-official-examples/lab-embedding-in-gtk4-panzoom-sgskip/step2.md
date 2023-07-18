# Import Libraries

Import the necessary libraries for this lab: GTK4, Matplotlib, and NumPy.

```python
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk4 import NavigationToolbar2GTK4 as NavigationToolbar
from matplotlib.backends.backend_gtk4agg import FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
```
