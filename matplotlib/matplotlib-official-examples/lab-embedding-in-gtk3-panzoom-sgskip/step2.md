# Create a GTK3 Window

Next, we will create a GTK3 window with a title, default size, and connect the "delete-event" signal to `Gtk.main_quit` function to close the window when the close button is clicked.

```python
win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK3")
```
