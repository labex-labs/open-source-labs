# モデルを作成する

このステップでは、データを格納するモデルを作成します。

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
