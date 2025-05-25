# Importar Bibliotecas

Primeiramente, precisamos importar as bibliotecas necessárias. Usaremos Matplotlib, GTK3 e o módulo Gtk do gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
