# Создание модели

Наконец, вам нужно создать модель для хранения данных.

```python
    def create_model(self):
        types = [float] * self.num_cols
        store = Gtk.ListStore(*types)
        for row in self.data:
            it = store.insert(-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store
```
