# データマネージャウィンドウを作成する

このステップでは、`Gtk.Window` クラスから拡張された `DataManager` クラスを作成します。このクラスは、描画したいデータの管理を担当します。

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
