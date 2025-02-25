# Créer le modèle

Dans cette étape, nous allons créer le modèle qui stockera nos données.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
