# Create a Scrolled Window

In order to display the Matplotlib figure, we will need to create a `Gtk.ScrolledWindow` widget. This will allow us to scroll through the figure if it is too large to fit in the window. We will also set the border width and add the scrolled window to the GTK3 window.

```python
sw = Gtk.ScrolledWindow()
win.add(sw)
sw.set_border_width(10)
```
