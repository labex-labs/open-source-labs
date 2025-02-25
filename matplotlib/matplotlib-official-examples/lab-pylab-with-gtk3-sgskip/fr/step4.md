# Ajouter un bouton à la barre d'outils

Nous allons ajouter un bouton à la barre d'outils en utilisant le module Gtk. Tout d'abord, nous créons un bouton avec une étiquette et le connectons à une fonction pour afficher un message lorsqu'il est cliqué. Ensuite, nous créons un élément d'outil, définissons son texte d'aide, ajoutons le bouton à celui-ci et l'insérons dans la barre d'outils.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # où insérer cela dans la barre d'outils
toolbar.insert(toolitem, pos)
```
