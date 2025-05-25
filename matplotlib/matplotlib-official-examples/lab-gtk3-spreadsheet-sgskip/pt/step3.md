# Configurar a Janela

Nesta etapa, configuraremos a janela que exibirá nossos dados. Começaremos inicializando a janela com um título e um tamanho.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
