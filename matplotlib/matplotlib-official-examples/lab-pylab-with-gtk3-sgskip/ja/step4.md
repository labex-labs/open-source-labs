# ツールバーにボタンを追加する

Gtkモジュールを使ってツールバーにボタンを追加します。まず、ラベル付きのボタンを作成し、クリックされたときにメッセージを表示する関数に接続します。次に、ツールアイテムを作成し、そのツールチップテキストを設定し、ボタンを追加してから、ツールバーに挿入します。

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # これをツールバーのどこに挿入するか
toolbar.insert(toolitem, pos)
```
