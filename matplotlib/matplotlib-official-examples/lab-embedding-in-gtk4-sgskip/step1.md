# Import the necessary libraries

```python
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import numpy as np
from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
```

We will use GTK4, numpy, and Matplotlib in this lab.
