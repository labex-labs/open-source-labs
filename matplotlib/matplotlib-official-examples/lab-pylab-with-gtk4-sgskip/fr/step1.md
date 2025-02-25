# Importez les bibliothèques requises

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

Nous importons les bibliothèques requises, y compris `matplotlib`, `gi`, `pyplot` et `Gtk`. Nous définissons le backend de matplotlib pour utiliser GTK4.
