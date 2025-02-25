# Importar bibliotecas

Primero, necesitamos importar las bibliotecas necesarias. Vamos a utilizar Matplotlib, GTK3 y el módulo Gtk del gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # o 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
