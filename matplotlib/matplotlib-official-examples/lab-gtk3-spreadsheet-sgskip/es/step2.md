# Crear la ventana del administrador de datos

En este paso, crearemos la clase `DataManager` que hereda de la clase `Gtk.Window`. Esta clase se encargará de administrar los datos que queremos representar gráficamente.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
