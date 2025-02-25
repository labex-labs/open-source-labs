# Ajouter une étiquette au conteneur vertical (VBox)

Nous allons ajouter une étiquette au conteneur vertical (VBox) pour afficher les coordonnées x,y de la souris lorsqu'elle est déplacée sur l'axe. Tout d'abord, nous créons une étiquette avec du texte et l'ajoutons au conteneur vertical (VBox).

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
