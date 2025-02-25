# Einrichten der Umgebung

Bevor wir beginnen, müssen wir unsere Umgebung einrichten. Wir starten damit, eine neue Python-Datei zu erstellen und die erforderlichen Bibliotheken zu importieren.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
