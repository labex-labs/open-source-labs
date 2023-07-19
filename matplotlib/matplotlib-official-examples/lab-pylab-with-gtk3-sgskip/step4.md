# Add Button to Toolbar

We will add a button to the toolbar using the Gtk module. First, we create a button with a label and connect it to a function to print a message when clicked. Then, we create a toolitem, set its tooltip text, add the button to it, and insert it into the toolbar.

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
