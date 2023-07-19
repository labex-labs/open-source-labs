# Create a GTK3 Window

The first step is to create a GTK3 window using the `Gtk.Window` class. We will also set the window's size and title, and connect the `delete-event` signal to the `Gtk.main_quit` function so that the window can be closed.

```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK3")
```
