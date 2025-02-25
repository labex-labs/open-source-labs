# Agregar un botón a la barra de herramientas

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

Creamos un botón con una etiqueta y una información emergente, y lo conectamos a una función que imprime un mensaje en la consola. Agregamos el botón a la barra de herramientas.
