# Création du graphique

Maintenant, nous pouvons commencer à créer notre graphique. Tout d'abord, importez les bibliothèques nécessaires et définissez la classe `Window1Signals`. Cette classe gérera le signal `destroy` pour la fenêtre.

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
