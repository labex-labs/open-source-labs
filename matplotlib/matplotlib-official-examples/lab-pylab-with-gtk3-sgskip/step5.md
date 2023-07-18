# Add Label to VBox

We will add a label to the vbox to display the x,y coordinates of the mouse when it is dragged over the axis. First, we create a label with some text and add it to the vbox.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
