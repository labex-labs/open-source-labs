# ツリービューを追加する

このステップでは、データを表示するツリービューをウィンドウに追加します。また、データを格納するモデルも作成します。

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
