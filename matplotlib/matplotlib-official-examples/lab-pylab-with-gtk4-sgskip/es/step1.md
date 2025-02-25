# Importar las bibliotecas necesarias

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

Importamos las bibliotecas necesarias, incluyendo `matplotlib`, `gi`, `pyplot` y `Gtk`. Establecemos el backend de matplotlib para usar GTK4.
