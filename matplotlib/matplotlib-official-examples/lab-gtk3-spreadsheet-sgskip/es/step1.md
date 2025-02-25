# Configurar el entorno

Antes de comenzar, necesitamos configurar nuestro entorno. Empezaremos creando un nuevo archivo de Python e importando las bibliotecas necesarias.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
