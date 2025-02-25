# Creación del gráfico

Ahora podemos comenzar a crear nuestro gráfico. Primero, importe las bibliotecas necesarias y defina la clase `Window1Signals`. Esta clase manejará la señal `destroy` para la ventana.

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
