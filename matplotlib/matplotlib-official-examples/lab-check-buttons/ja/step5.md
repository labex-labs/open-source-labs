# コールバック関数の定義

チェックボタン用のコールバック関数を定義する必要があります。この関数は、チェックボタンがクリックされるたびに呼び出されます。この関数を使って、プロット上の対応する線の可視性を切り替えます。

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
