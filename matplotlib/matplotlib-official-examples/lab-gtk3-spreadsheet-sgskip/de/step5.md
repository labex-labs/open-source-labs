# Fügen Sie eine TreeView hinzu

In diesem Schritt fügen wir einer TreeView zum Fenster hinzu, die unsere Daten anzeigen wird. Wir erstellen auch ein Modell, um die Daten zu speichern.

```python
sw = Gtk.ScrolledWindow()
sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
vbox.pack_start(sw, True, True, 0)
model = self.create_model()
self.treeview = Gtk.TreeView(model=model)
self.treeview.connect('row-activated', self.plot_row)
sw.add(self.treeview)
self.add_columns()
```
