# Ajouter une barre d'outils

Ajoutez une barre d'outils à l'application qui permet à l'utilisateur de zoomer, de panser et d'enregistrer le tracé sous forme d'image. Cette barre d'outils est ajoutée en bas du cadre.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
