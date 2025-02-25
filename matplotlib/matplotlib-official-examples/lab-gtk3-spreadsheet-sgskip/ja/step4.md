# ラベルを追加する

このステップでは、ウィンドウにラベルを追加します。このラベルは、ユーザーに行をダブルクリックしてデータを描画するよう促すものです。

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
