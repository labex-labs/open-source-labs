# Create a GTK4 ScrolledWindow and set the margin

```python
sw = Gtk.ScrolledWindow(margin_top=10, margin_bottom=10,
                        margin_start=10, margin_end=10)
win.set_child(sw)
```

We create a GTK4 ScrolledWindow and set the margin to 10 pixels on each side. We then set the ScrolledWindow as the child of the application window.
