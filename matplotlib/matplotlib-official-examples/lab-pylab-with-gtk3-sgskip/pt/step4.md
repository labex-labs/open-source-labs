# Adicionar Botão à Toolbar

Adicionaremos um botão à toolbar usando o módulo Gtk. Primeiro, criamos um botão com um rótulo e o conectamos a uma função para imprimir uma mensagem quando clicado. Em seguida, criamos um `toolitem`, definimos seu texto de dica de ferramenta (tooltip), adicionamos o botão a ele e o inserimos na toolbar.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # where to insert this in the toolbar
toolbar.insert(toolitem, pos)
```
