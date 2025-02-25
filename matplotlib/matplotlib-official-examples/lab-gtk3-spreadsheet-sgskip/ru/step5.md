# Добавьте TreeView

В этом шаге мы добавим TreeView в окно, которое будет отображать наши данные. Также мы создадим модель для хранения данных.

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
