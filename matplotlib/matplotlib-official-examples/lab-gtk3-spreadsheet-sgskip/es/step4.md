# Agregar una etiqueta

En este paso, agregaremos una etiqueta a la ventana que le pedirá al usuario que haga doble clic en una fila para graficar los datos.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
