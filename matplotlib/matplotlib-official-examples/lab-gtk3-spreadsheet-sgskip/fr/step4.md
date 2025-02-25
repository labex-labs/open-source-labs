# Ajouter une étiquette

Dans cette étape, nous allons ajouter une étiquette à la fenêtre qui invitera l'utilisateur à double-cliquer sur une ligne pour tracer les données.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double cliquez sur une ligne pour tracer les données')
vbox.pack_start(label, False, False, 0)
```
