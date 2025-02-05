# Create the Data Manager Window

In this step, we'll create the `DataManager` class that extends from the `Gtk.Window` class. This class will be responsible for managing the data that we want to plot.

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
