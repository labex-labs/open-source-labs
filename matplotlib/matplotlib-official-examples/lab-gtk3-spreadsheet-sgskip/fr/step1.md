# Configuration de l'environnement

Avant de commencer, nous devons configurer notre environnement. Nous allons commencer par créer un nouveau fichier Python et en importer les bibliothèques nécessaires.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
