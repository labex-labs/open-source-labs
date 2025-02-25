# Создайте окно менеджера данных

В этом шаге мы создадим класс `DataManager`, который наследуется от класса `Gtk.Window`. Этот класс будет отвечать за управление данными, которые мы хотим отобразить.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
