# AnnotatedCursor クラスを作成する

`matplotlib.widgets.Cursor` から継承した新しいクラス `AnnotatedCursor` を作成し、新しいウィジェットの作成とそれらのイベントコールバックの実装を示します。`AnnotatedCursor` クラスは、現在の座標を表示するテキスト付きの十字マーカーカーソルを作成するために使用されます。

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
   ...
    """
```
