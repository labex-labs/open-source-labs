# モデルの作成

最後に、データを格納するモデルを作成する必要があります。

```python
    def create_model(self):
        types = [float] * self.num_cols
        store = Gtk.ListStore(*types)
        for row in self.data:
            it = store.insert(-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store
```
