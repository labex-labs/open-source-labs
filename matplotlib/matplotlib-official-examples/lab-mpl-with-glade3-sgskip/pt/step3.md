# Criando o Gráfico

Agora podemos começar a criar nosso gráfico. Primeiro, importe as bibliotecas necessárias e defina a classe `Window1Signals`. Esta classe irá lidar com o sinal `destroy` para a janela.

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
