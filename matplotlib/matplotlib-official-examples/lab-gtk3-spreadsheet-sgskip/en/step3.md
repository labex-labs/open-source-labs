# Set Up the Window

In this step, we'll set up the window that will display our data. We'll start by initializing the window with a title and a size.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
