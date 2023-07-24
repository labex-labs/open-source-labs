# Add a Label

In this step, we'll add a label to the window that will prompt the user to double-click a row to plot the data.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
