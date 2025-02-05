# Add a label to the canvas

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

We create a label and set its text. We add the label to the vbox after the figure canvas.
