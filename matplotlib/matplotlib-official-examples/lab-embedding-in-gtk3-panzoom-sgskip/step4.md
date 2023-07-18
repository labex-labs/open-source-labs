# Add Figure Canvas and Navigation Toolbar to GTK3 Window

Next, we will add a Matplotlib figure canvas to the GTK3 window using a `Gtk.VBox` container. We will also add a navigation toolbar to the window using `NavigationToolbar` and pack it into the same `Gtk.VBox` container.

```python
vbox = Gtk.VBox()
win.add(vbox)

# Add canvas to vbox
canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
vbox.pack_start(canvas, True, True, 0)

# Create toolbar
toolbar = NavigationToolbar(canvas)
vbox.pack_start(toolbar, False, False, 0)
```
