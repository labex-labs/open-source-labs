# Agregar una etiqueta al VBox

Agregaremos una etiqueta al vbox para mostrar las coordenadas x,y del mouse cuando se arrastra sobre el eje. Primero, creamos una etiqueta con algún texto y la agregamos al vbox.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
