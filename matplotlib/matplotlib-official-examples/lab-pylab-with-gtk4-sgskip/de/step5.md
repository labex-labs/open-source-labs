# Fügen eines Labels zur Zeichenfläche hinzu

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

Wir erstellen ein Label und setzen seinen Text. Wir fügen das Label zur vertikalen Box (vbox) hinter der Figurzeichenfläche hinzu.
