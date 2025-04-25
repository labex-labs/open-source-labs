# VBox にラベルを追加する

マウスを軸の上をドラッグしたときの x,y 座標を表示するために、VBox にラベルを追加します。まず、いくつかのテキスト付きのラベルを作成し、VBox に追加します。

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
