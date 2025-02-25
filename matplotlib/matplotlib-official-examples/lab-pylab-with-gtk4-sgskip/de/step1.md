# Importieren der erforderlichen Bibliotheken

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

Wir importieren die erforderlichen Bibliotheken, einschließlich `matplotlib`, `gi`, `pyplot` und `Gtk`. Wir setzen den Backend von matplotlib, um GTK4 zu verwenden.
