# Erstellen des Graphen

Jetzt können wir beginnen, unseren Graphen zu erstellen. Zunächst importieren wir die erforderlichen Bibliotheken und definieren die Klasse `Window1Signals`. Diese Klasse wird das Signal `destroy` für das Fenster verarbeiten.

```python
from pathlib import Path

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import numpy as np

from matplotlib.backends.backend_gtk3agg import \
    FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure


class Window1Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()
```
