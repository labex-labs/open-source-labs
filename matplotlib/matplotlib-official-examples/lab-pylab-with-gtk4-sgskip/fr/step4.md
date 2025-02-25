# Ajoutez un bouton à la barre d'outils

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

Nous créons un bouton avec une étiquette et une info-bulle, et le connectons à une fonction qui imprime un message dans la console. Nous ajoutons le bouton à la barre d'outils.
