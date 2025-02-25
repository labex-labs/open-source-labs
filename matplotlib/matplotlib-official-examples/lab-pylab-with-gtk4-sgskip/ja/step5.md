# キャンバスにラベルを追加する

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

ラベルを作成してそのテキストを設定します。グラフキャンバスの後にラベルを vbox に追加します。
