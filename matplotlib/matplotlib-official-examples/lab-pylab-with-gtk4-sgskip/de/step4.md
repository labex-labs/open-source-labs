# Fügen eines Buttons zur Symbolleiste hinzu

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

Wir erstellen einen Button mit einem Label und einem Tooltip und verbinden ihn mit einer Funktion, die eine Nachricht in die Konsole ausgibt. Wir fügen den Button zur Symbolleiste hinzu.
