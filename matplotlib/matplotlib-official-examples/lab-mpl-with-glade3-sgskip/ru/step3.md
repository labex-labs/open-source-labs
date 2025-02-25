# Создание графика

Теперь мы можем начать создавать нашу диаграмму. Сначала импортируем необходимые библиотеки и определим класс `Window1Signals`. Этот класс будет обрабатывать сигнал `destroy` для окна.

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
