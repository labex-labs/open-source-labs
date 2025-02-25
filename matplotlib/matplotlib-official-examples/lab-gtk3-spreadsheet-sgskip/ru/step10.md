# Создайте модель

В этом шаге мы создадим модель, которая будет хранить наши данные.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
