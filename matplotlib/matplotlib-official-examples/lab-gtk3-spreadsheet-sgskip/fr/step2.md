# Créer la fenêtre de gestion des données

Dans cette étape, nous allons créer la classe `DataManager` qui hérite de la classe `Gtk.Window`. Cette classe sera responsable de la gestion des données que nous voulons tracer.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
