# Importar as bibliotecas necessárias

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

Importamos as bibliotecas necessárias, incluindo `matplotlib`, `gi`, `pyplot` e `Gtk`. Definimos o backend do matplotlib para usar GTK4.
