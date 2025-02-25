# Импортируем необходимые библиотеки

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

Мы импортируем необходимые библиотеки, включая `matplotlib`, `gi`, `pyplot` и `Gtk`. Мы настраиваем бэкенд `matplotlib` для использования GTK4.
