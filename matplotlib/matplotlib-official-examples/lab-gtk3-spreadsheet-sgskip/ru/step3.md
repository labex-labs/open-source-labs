# Настройка окна

В этом шаге мы настроим окно, которое будет отображать наши данные. Мы начнем с инициализации окна с заголовком и размером.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
