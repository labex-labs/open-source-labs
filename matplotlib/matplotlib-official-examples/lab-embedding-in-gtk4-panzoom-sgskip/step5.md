# Add the Canvas

Add a canvas to the GTK4 window. The canvas is a Gtk.DrawingArea that contains the Matplotlib Figure.

```python
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
win.set_child(vbox)

canvas = FigureCanvas(fig)
canvas.set_hexpand(True)
canvas.set_vexpand(True)
vbox.append(canvas)
```
