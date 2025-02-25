# Bibliotheken importieren

Zunächst müssen wir die erforderlichen Bibliotheken importieren. Wir werden Matplotlib, GTK3 und das Gtk-Modul aus dem gi.repository verwenden.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # oder 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
