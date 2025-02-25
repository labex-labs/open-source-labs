# キー入力イベント関数の定義

次に、キーが押されたときに呼び出される `on_press` 関数を定義します。この関数は、押されたキーに関する情報を含む `event` パラメータを受け取ります。この例では、「x」キーが押されたときに x 軸のラベルの表示を切り替えます。

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
