# Fügen Sie eine Bezeichnung hinzu

In diesem Schritt fügen wir einem Fenster eine Bezeichnung hinzu, die den Benutzer auffordert, auf eine Zeile zu doppelklicken, um die Daten zu plotten.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
