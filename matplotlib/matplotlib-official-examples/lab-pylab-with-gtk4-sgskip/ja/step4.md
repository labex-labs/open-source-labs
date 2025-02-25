# ツールバーにボタンを追加する

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

ラベルとツールチップ付きのボタンを作成し、コンソールにメッセージを出力する関数に接続します。ボタンをツールバーに追加します。
