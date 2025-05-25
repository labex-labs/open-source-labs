# Criar o Modelo

Nesta etapa, criaremos o modelo que armazenará nossos dados.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
