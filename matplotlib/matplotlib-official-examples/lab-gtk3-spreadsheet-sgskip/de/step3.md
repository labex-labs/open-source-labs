# Fenster einrichten

In diesem Schritt werden wir das Fenster einrichten, in dem unsere Daten angezeigt werden. Wir beginnen damit, das Fenster mit einem Titel und einer Größe zu initialisieren.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
