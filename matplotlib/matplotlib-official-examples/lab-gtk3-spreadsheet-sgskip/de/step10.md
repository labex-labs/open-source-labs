# Modell erstellen

In diesem Schritt erstellen wir das Modell, das unsere Daten speichern wird.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
