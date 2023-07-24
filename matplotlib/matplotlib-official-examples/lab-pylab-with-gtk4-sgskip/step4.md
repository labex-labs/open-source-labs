# Add a button to the toolbar

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

We create a button with a label and a tooltip, and connect it to a function that prints a message to the console. We add the button to the toolbar.
