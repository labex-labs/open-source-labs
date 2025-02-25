# VBoxにラベルを追加する

マウスを軸の上をドラッグしたときのx,y座標を表示するために、VBoxにラベルを追加します。まず、いくつかのテキスト付きのラベルを作成し、VBoxに追加します。

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
