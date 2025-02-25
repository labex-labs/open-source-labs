# Configuration de la fenêtre

Dans cette étape, nous allons configurer la fenêtre qui affichera nos données. Nous commencerons par initialiser la fenêtre avec un titre et une taille.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
