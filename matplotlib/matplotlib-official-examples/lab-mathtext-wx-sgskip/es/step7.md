# Agregar una barra de herramientas

Agrega una barra de herramientas a la aplicación que permite al usuario hacer zoom in y out, desplazarse y guardar la gráfica como una imagen. Esta barra de herramientas se agrega al fondo del marco.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
