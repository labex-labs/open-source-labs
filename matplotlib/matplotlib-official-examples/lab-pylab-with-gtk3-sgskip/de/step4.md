# Button zur Toolbar hinzufügen

Wir werden einen Button zur Toolbar hinzufügen, indem wir das Gtk-Modul verwenden. Zunächst erstellen wir einen Button mit einem Label und verbinden ihn mit einer Funktion, die eine Nachricht ausgibt, wenn der Button geklickt wird. Anschließend erstellen wir ein Toolitem, legen dessen Tooltip-Text fest, fügen den Button hinzu und fügen es in die Toolbar ein.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # wo dieses in der Toolbar eingefügt werden soll
toolbar.insert(toolitem, pos)
```
