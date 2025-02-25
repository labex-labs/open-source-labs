# Ajoutez une étiquette à la toile

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

Nous créons une étiquette et définissons son texte. Nous ajoutons l'étiquette au conteneur vertical (vbox) après la toile de la figure.
