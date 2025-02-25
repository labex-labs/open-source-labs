# 選択コールバック関数を定義する

ユーザーが四角形または楕円を選択するたびに、選択コールバック関数が呼び出されます。この関数は、クリックと解放イベントを引数として受け取り、四角形または楕円の座標を表示します。

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
