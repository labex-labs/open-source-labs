# Erstellen des Datenmanagers-Fensters

In diesem Schritt werden wir die Klasse `DataManager` erstellen, die von der Klasse `Gtk.Window` erbt. Diese Klasse wird für das Verwalten der Daten verantwortlich sein, die wir plotten möchten.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
