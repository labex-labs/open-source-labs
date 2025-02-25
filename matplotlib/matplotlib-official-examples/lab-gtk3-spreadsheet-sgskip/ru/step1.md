# Настройка среды

Прежде чем начать, нам нужно настроить нашу среду. Мы начнем с создания нового файла Python и импорта необходимых библиотек.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
