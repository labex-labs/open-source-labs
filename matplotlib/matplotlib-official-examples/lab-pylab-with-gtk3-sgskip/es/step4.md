# Agregar un botón a la barra de herramientas

Agregaremos un botón a la barra de herramientas utilizando el módulo Gtk. Primero, creamos un botón con una etiqueta y lo conectamos a una función para imprimir un mensaje cuando se haga clic en él. Luego, creamos un elemento de herramienta, establecemos su texto de ayuda, agregamos el botón a él e insertamos el elemento de herramienta en la barra de herramientas.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # donde insertar esto en la barra de herramientas
toolbar.insert(toolitem, pos)
```
