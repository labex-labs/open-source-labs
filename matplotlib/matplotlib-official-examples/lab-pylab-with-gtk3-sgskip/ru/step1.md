# Импорт библиотек

Во - первых, нам нужно импортировать необходимые библиотеки. Мы будем использовать Matplotlib, GTK3 и модуль Gtk из gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # или 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
