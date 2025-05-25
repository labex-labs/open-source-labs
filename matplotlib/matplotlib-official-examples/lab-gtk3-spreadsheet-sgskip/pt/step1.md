# Configurando o Ambiente

Antes de começar, precisamos configurar nosso ambiente. Começaremos criando um novo arquivo Python e importando as bibliotecas necessárias.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
