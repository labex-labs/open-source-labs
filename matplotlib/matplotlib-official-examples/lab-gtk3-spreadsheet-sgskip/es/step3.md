# Configurar la ventana

En este paso, configuraremos la ventana que mostrará nuestros datos. Empezaremos inicializando la ventana con un título y un tamaño.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
