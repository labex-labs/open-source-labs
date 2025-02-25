# Agregar una etiqueta al lienzo

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

Creamos una etiqueta y establecemos su texto. Agregamos la etiqueta al contenedor vertical (vbox) después del lienzo de la figura.
